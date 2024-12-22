from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import BaseModel

class Team(BaseModel):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    users = relationship("User", back_populates="team")