from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {}

class UserCreate(BaseModel):
    username: str
    password: str

@router.post("/signup")
def signup(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_pw = pwd_context.hash(user.password)
    fake_users_db[user.username] = {"username": user.username, "password": hashed_pw}
    return {"message": f"User {user.username} created"}

@router.post("/login")
def login(user: UserCreate):
    stored_user = fake_users_db.get(user.username)
    if not stored_user or not pwd_context.verify(user.password, stored_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": f"Welcome back, {user.username}"}
