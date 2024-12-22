from sqlalchemy.orm import Session
from crud.user_crud import UserCRUD
from schemas.user_schema import UserCreate, UserUpdate

class UserService:
    def __init__(self, db: Session, crud: UserCRUD):
        self.db = db
        self.crud = crud

    def list_users(self, skip: int = 0, limit: int = 10):
        return self.crud.get_users(self.db, skip=skip, limit=limit)

    def get_user(self, user_id: int):
        user = self.crud.get_user(self.db, user_id=user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def create_user(self, user: UserCreate):
        return self.crud.create_user(self.db, user=user)

    def update_user(self, user_id: int, user: UserUpdate):
        return self.crud.update_user(self.db, user_id=user_id, user=user)

    def delete_user(self, user_id: int):
        return self.crud.delete_user(self.db, user_id=user_id)