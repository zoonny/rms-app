from sqlalchemy import or_
from sqlalchemy.orm import Session
from pprint import pprint
from db.database import SessionLocal
from models import Member, Project, Team, User, WeeklyReport, ProjectMember
from datetime import datetime, date

def query(session: Session):
    team: Team = session.query(Team).filter(Team.name == '전략개발팀').first()
    pprint(team)
    for member in team.members:
        # print(f'사번:{member.id}, 성명:{member.name}')
        for project_link in member.project_links:
            project: Project = project_link.project
            print(f'사번:{member.id}, 성명:{member.name}, 프로젝트:{project.name}')

            for member_link in project.member_links:
                project_member: Member = member_link.member
                if member.id != project_member.id:
                    print(f'협업멤버 - 사번:{project_member.id}, 성명:{project_member.name}')

    # project: Project = session.query(Project).filter(Project.name == '하나은행').first()
    # print(vars(project))
    # print(len(project.member_links))
    # for member_link in project.member_links:
    #     print(member_link.member.name)

query(SessionLocal())
