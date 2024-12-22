from pydantic import ConfigDict, BaseModel
from datetime import datetime

class MemberBase(BaseModel):
    employee_id: str
    name: str
    position: str

class MemberCreate(MemberBase):
    pass

class MemberUpdate(MemberBase):
    pass

class MemberResponse(MemberBase):
    id: int

    model_config = ConfigDict(from_attributes=True)