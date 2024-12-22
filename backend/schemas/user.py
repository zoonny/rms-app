from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: int