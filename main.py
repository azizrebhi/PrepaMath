from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import retrieval 
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)




# Include your auth router

app.include_router(retrieval.router)




@app.get("/")
async def root():
    return {"message": "Server is running"}