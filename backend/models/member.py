# __all__ = ["Member"]  # export할 객체 정의

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel

class Member(BaseModel):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True)
    name = Column(String, index=True)
    position = Column(String, nullable=False)
    team_id = Column(Integer)   # ForeignKeyConstraint 생략
    # team_id = Column(Integer, ForeignKey("teams.id"))   # ForeignKey 추가

    # Relationship 정의
    team = relationship("Team", back_populates="members")