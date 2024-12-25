from pydantic import ConfigDict, BaseModel
from models.member import Member

class MemberBase(BaseModel):
    id: str
    employee_id: str
    name: str
    position: str

class MemberCreate(MemberBase):
    def to_model(self):
        member = Member(
            employee_id=self.employee_id,
            name=self.name,
            position=self.position)
        return member
    pass

class MemberUpdate(MemberBase):
    def update_model(self, member: Member):
        member.employee_id = self.employee_id
        member.name = self.name
        member.position = self.position
        return
    pass

class MemberResponse(MemberBase):
    id: int

    model_config = ConfigDict(from_attributes=True)