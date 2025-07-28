from fastapi import FastAPI
from app.routers import auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Welcome to the YUGO backend 🚀"}
