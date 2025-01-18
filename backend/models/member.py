# __all__ = ["Member"]  # export할 객체 정의

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel
# from models.project_member import project_member
from models.task import member_task

class Member(BaseModel):
    __tablename__ = "member"

    id = Column(String, primary_key=True, index=True)
    employee_id = Column(String, unique=False, nullable=True)   # 2사번
    name = Column(String, index=True)
    position = Column(String, nullable=False)
    # team_id = Column(String)   # ForeignKeyConstraint 생략
    team_id = Column(String, ForeignKey("team.id"))   # ForeignKey 추가

    # Relationship 정의
    team = relationship("Team", back_populates="members")
    # primaryjoin 사용 : 아래 오류 해결
    # sqlalchemy.exc.NoForeignKeysError: Could not determine join condition between parent/child tables on relationship Member.team - there are no foreign keys linking these tables.  Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint, or specify a 'primaryjoin' expression.
    # team = relationship("Team", primaryjoin="Member.team_id == Team.id")
    # cascade 활성화
    # team = relationship("Team", back_populates="members", cascade="all, delete")

    # 관계 설정
    project_links = relationship('ProjectMember', back_populates='member')
    # weekly_reports = relationship('WeeklyReport', back_populates='member')
    weekly_reports = relationship(
        'WeeklyReport',
        primaryjoin='Member.id == WeeklyReport.member_id',
        back_populates='member',
        foreign_keys='WeeklyReport.member_id',
        lazy='selectin'
    )
    # task_links = relationship('MemberTask', back_populates='member')
    tasks = relationship(
        'Task',
        secondary=member_task,
        back_populates='members'
    )
