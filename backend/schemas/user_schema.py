from pydantic import ConfigDict, BaseModel
from datetime import datetime
from models.user import User
# 아래 BaseModel로 생성 시 오류
# from db.database import BaseModel

class UserBase(BaseModel):
    email: str
    name: str
    password: str
    # is_active: int

    # model_config = ConfigDict(from_attributes=True)
    class Config:
        orm_mode = True
    

class UserCreate(UserBase):
    def to_model(self):
        user = User(
            email=self.email,
            name=self.name, 
            password=None)
        return user 
    pass

class UserUpdate(UserBase):
    def update_model(self, user: User):
        user.email = self.email,
        user.name = self.name,
        user.hashed_password = self.password,
        # user.is_active = self.is_active
        return
    pass

class UserResponse(UserBase):
    id: int
    email: str