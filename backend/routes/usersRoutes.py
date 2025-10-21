# routes/user_routes.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionDep
from models.user import User
from models.chat import Chat
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import timedelta
from utils.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/users", tags=["Users"])


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "citizen"


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    created_at: str

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/signup", response_model=UserResponse)
def register_user(user: UserCreate, db: SessionDep):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)
    new_user = User(
        name=user.name, email=user.email, password=hashed_pw, role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=TokenResponse)
def login_user(request: LoginRequest, db: SessionDep):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": str(user.id), "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/", response_model=List[UserResponse])
def get_users(db: SessionDep):
    return db.query(User).all()


@router.get("/{user_id}")
def get_user(user_id: int, db: SessionDep):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    chats = db.query(Chat).filter(Chat.user_id == user_id).all()
    return {
        "user": user,
        "chats": [
            {
                "id": c.id,
                "question": c.question,
                "answer": c.answer,
                "notebook": c.notebook_name,
            }
            for c in chats
        ],
    }


@router.delete("/{user_id}")
def delete_user(user_id: int, db: SessionDep):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": f"User {user_id} deleted successfully"}
