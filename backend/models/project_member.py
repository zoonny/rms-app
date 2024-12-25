from sqlalchemy import Column, Integer, String, DateTime, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel

class ProjectMember(BaseModel):
    __tablename__ = "project_member"

    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True)
    member_id = Column(String, ForeignKey('member.id'), primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    # 관계 설정
    project = relationship('Project', back_populates='member_links')
    member = relationship('Member', back_populates='project_links')

# 중간 테이블로 사용되는 ProjectMember는 Table 객체로 정의되어야 함
# 매핑된 클래스가 아닌 Table 객체를 secondary로 전달
# project_member = Table(
#     'project_member', 
#     BaseModel.metadata,
#     Column('project_id', Integer, ForeignKey('project.id'), primary_key=True),
#     Column('member_id', String, ForeignKey('member.id'), primary_key=True),
#     Column('start_time', Date, nullable=False),
#     Column('end_time', Date, nullable=False),
# )