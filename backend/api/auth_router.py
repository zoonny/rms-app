from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.logger import logger
from db.database import get_db
from schemas.user_schema import UserResponse, UserCreate
from models.user import User
from datetime import timedelta
from utils import auth

router = APIRouter()

def get_auth_service(db: Session = Depends(get_db)):
    pass

# 회원 가입
@router.post("/auth/signup", response_model=UserCreate)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = auth.hash_password(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

# 토큰 발급
@router.post("/auth/signin")
def signin(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/auth/me")
def read_auth_me(current_user: str = Depends(auth.verify_token)):
    return {"email": current_user}
