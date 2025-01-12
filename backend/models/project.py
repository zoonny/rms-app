from sqlalchemy import Column, Integer, String, DateTime, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel
# from models.project_member import project_member

class Project(BaseModel):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    # 관계 설정
    member_links = relationship('ProjectMember', back_populates='project')

    def __repr__(self):
        return f"Project(id={self.id}, name={self.name}, start_date={self.start_date}, end_date={self.end_date})"
