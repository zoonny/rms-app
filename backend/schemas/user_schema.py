from pydantic import ConfigDict, BaseModel
from datetime import datetime
# 아래 BaseModel로 생성 시 오류
# from db.database import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    # created_at: datetime
    # updated_at: datetime
    

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)