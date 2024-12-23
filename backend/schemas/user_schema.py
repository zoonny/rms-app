from pydantic import ConfigDict, BaseModel
from datetime import datetime
from models.user import User
# 아래 BaseModel로 생성 시 오류
# from db.database import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    # created_at: datetime
    # updated_at: datetime
    

class UserCreate(UserBase):
    def to_model(self):
        user = User(
            name=self.name, 
            email=self.email)
        return user 
    pass

class UserUpdate(UserBase):
    def update_model(self, user: User):
        user.name = self.name
        user.email = self.email
        return
    pass

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)