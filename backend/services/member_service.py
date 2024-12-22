from sqlalchemy.orm import Session
from crud.member_crud import MemberCRUD
from schemas.member_schema import MemberCreate, MemberUpdate

class MemberService:
    def __init__(self, db: Session, crud: MemberCRUD):
        self.db = db
        self.crud = crud

    def list_members(self, skip: int = 0, limit: int = 10):
        return self.crud.get_members(self.db, skip=skip, limit=limit)

    def get_member(self, member_id: int):
        member = self.crud.get_member(self.db, member_id=member_id)
        if not member:
            raise ValueError("member not found")
        return member 

    def create_member(self, member: MemberCreate):
        return self.crud.create_member(self.db, member=member)

    def update_member(self, member_id: int, member: MemberUpdate):
        return self.crud.update_member(self.db, member_id=member_id, member=member)

    def delete_member(self, member_id: int):
        return self.crud.delete_member(self.db, member_id=member_id)