from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel

# Member Class
# team = relationship("Team", back_populates="members")

# Team Class
# members = relationship("Member", back_populates="team")

class Team(BaseModel):
    __tablename__ = "team"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)

    # Relationship 정의
    members = relationship("Member", back_populates="team")