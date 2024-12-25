from sqlalchemy import or_
from sqlalchemy.orm import Session
from pprint import pprint
from db.database import SessionLocal
from models import Member, Project, Team, User, WeeklyReport, ProjectMember
from datetime import datetime, date

def insert_project_member(session: Session):
    project: Project = session.query(Project).filter(Project.name == '하나은행').first()
    members = session.query(Member).filter(or_(Member.name == '권성광', Member.name == '이명진')).all()
    for member in members:
        project_member = ProjectMember(project=project, member=member, start_date=datetime.now(), end_date=datetime.now())
        session.add(project_member)
    session.commit()

insert_project_member(SessionLocal())
