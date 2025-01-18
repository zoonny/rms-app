from sqlalchemy import Column, Integer, String, DateTime, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel

member_task = Table(
    'member_task',
    BaseModel.metadata,
    Column('member_id', String, ForeignKey('member.id'), primary_key=True),
    Column('task_id', Integer, ForeignKey('task.id'), primary_key=True),
    Column('start_date', Date, nullable=False),
    Column('end_date', Date, nullable=False)
)

class Task(BaseModel):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    # 관계설정
    # member_links = relationship('MemberTask', back_populates='task')
    members = relationship(
        'Member',
        secondary=member_task,
        back_populates='tasks'
    )

    def __repr__(self):
        return f"Task(id={self.id}, name={self.name}, start_date={self.start_date}, end_date={self.end_date})"
