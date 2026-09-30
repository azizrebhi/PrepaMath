import traceback

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.auth import fastapi_users ,auth_backend, google_oauth_client, SECRET
from app.schema import UserRead , UserCreate
from app.routers import answer, chapters, retrieval

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)


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
# both rather than hardcoding one and re-editing this every time it shifts.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Include your auth router
app.include_router(fastapi_users.get_oauth_router(
    google_oauth_client,
    auth_backend,
    SECRET,
    redirect_url="http://localhost:5173/auth/google/callback",
    associate_by_email=True,
          ),
          prefix="/auth/google",
          tags=["auth"],
)
app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
app.include_router(retrieval.router)
app.include_router(chapters.router)
app.include_router(answer.router)




@app.get("/")
async def root():
    return {"message": "Server is running"}