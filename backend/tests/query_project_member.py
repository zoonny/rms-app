from sqlalchemy import or_
from sqlalchemy.orm import Session
from pprint import pprint
from db.database import SessionLocal
from models import Member, Project, Team, User, WeeklyReport, ProjectMember
from datetime import datetime, date

def query(session: Session):
    project: Project = session.query(Project).filter(Project.name == '하나은행').first()
    print(vars(project))
    print(len(project.member_links))
    for member_link in project.member_links:
        print(member_link.member.name)

query(SessionLocal())
