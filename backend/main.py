from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.auth import fastapi_users ,auth_backend
from app.schema import UserRead , UserCreate
from app.routers import answer, chapters, retrieval
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

# Vite's dev server picks a port (5173, falls back to 5174, ...) — allow
# both rather than hardcoding one and re-editing this every time it shifts.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include your auth router
app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
app.include_router(retrieval.router)
app.include_router(chapters.router)
app.include_router(answer.router)




@app.get("/")
async def root():
    return {"message": "Server is running"}