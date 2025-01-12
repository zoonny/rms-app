from sqlalchemy import Column, Integer, String, DateTime, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel

# class MemberTask(BaseModel):
#     __tablename__ = "member_task"

#     member_id = Column(String, ForeignKey('member.id'), primary_key=True)
#     task_id = Column(Integer, ForeignKey('task.id'), primary_key=True)
#     start_date = Column(Date, nullable=False)
#     end_date = Column(Date, nullable=False)

#     # 관계 설정
#     # member객체 = Member 사용, member.task_links 를 사용해 task에 접근
#     member = relationship('Member', back_populates='task_links')
#     # task객체 = Task 사용, task.member_links 로 member에 접근
#     task = relationship('Task', back_populates='member_links')

#     def __repr__(self):
#         return f"MemberTask(member_id={self.member_id}, task_id={self.task_id}, start_date={self.start_date}, end_date={self.end_date})"
