import os
import traceback

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.auth import fastapi_users ,auth_backend, google_oauth_client, SECRET
from app.rate_limit import limiter
from app.schema import UserRead , UserCreate, UserUpdate
from app.routers import answer, chapters, retrieval

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


# TEMPORARY — remove once the Google OAuth 500 is diagnosed. Forces the real
# exception into both the terminal and the response body, since something in
# this environment isn't surfacing tracebacks in the uvicorn console.
@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"detail": f"{type(exc).__name__}: {exc}"},
    )

# Vite's dev server picks a port (5173, falls back to 5174, ...) — allow
# both by default rather than hardcoding one and re-editing this every time
# it shifts. In production, set ALLOWED_ORIGINS to a comma-separated list
# (e.g. the deployed Vercel URL) — without it, the deployed frontend's
# requests get rejected by the browser's own CORS check before this app's
# code ever runs.
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:5174").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Include your auth router
app.include_router(fastapi_users.get_oauth_router(
    google_oauth_client,
    auth_backend,
    SECRET,
    # Must exactly match a redirect URI registered in Google's OAuth
    # console — Google rejects the callback outright on any mismatch, so
    # this has to point at the deployed frontend's URL in production, not
    # localhost.
    redirect_url=os.getenv("GOOGLE_OAUTH_REDIRECT_URL", "http://localhost:5173/auth/google/callback"),
    associate_by_email=True,
    # fastapi-users' CSRF cookie defaults to SameSite=Lax, which only
    # survives top-level navigations — but this flow calls /authorize and
    # /callback via fetch() from a different origin (Vercel frontend calling
    # the Render backend), not a page redirect. A Lax cookie set on one
    # cross-origin fetch silently never comes back on the next one, which
    # surfaces as an opaque "invalid state token" failure at /callback.
    # SameSite=None (paired with the already-default Secure=True) is what
    # cross-site fetch-based cookies actually require.
    csrf_token_cookie_samesite="none",
          ),
          prefix="/auth/google",
          tags=["auth"],
)
app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])
app.include_router(retrieval.router)
app.include_router(chapters.router)
app.include_router(answer.router)




@app.get("/")
async def root():
    return {"message": "Server is running"}