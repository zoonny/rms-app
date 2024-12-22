from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate, UserUpdate, UserResponse
from db.database import get_db
from services.user_service import UserService
from crud.user_crud import UserCRUD

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    crud = UserCRUD()
    return UserService(db=db, crud=crud)

@router.get("/users", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, user_service: UserService = Depends(get_user_service)):
    return user_service.list_users(skip=skip, limit=limit)

@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.get_user(user_id=user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/users", response_model=UserResponse)
def create_new_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.create_user(user=user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/users/{user_id}", response_model=UserResponse)
def update_existing_user(user_id: int, user: UserUpdate, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.update_user(user_id, user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/users/{user_id}")
def delete_existing_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))