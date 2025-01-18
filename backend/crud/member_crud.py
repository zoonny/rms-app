from core.logger import logger
from sqlalchemy import or_, func
from sqlalchemy.orm import Session
from models.member import Member 
from schemas.member_schema import MemberCreate, MemberUpdate

class MemberCRUD:
    def get_members(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Member).offset(skip).limit(limit).all()

    def get_member(self, db: Session, member_id: int):
        return db.query(Member).filter(Member.id == member_id).first()

    def create_member(self, db: Session, member: MemberCreate):
        db_member = member.to_model()
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member;

    def update_member(self, db: Session, member_id: int, member: MemberUpdate):
        db_member = db.query(Member).filter(Member.id == member_id).first()
        if db_member:
            member.update_model(db_member)
            db.commit()
            db.refresh(db_member)
        return db_member

    def delete_member(self, db: Session, member_id: int):
        db_member = db.query(Member).filter(Member.id == member_id).first()
        if db_member:
            db.delete(db_member)
            db.commit()
        return db_member

    def get_member_count(self, db: Session, team_id: str):
        return db.query(Member).filter(Member.team_id == team_id).count()
