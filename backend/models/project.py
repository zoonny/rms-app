from sqlalchemy import Column, Integer, String, DateTime
from models.base import BaseModel

class Project(BaseModel):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

class ProjectMember(BaseModel):
    __tablename__ = "project_member"

    project_id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
