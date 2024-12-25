from sqlalchemy import or_
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models import Member, Project, Team, User, WeeklyReport, ProjectMember
from datetime import datetime, date
import pprint

def insert_test_data(session: Session):
    # 데이터 초기화
    try:
        session.query(Member).delete()
        session.query(Team).delete()
        session.query(Project).delete()
        session.query(User).delete()
        session.query(ProjectMember).delete()
        session.commit()
    except Exception as e:
        print(e)

    # 테스트 데이터 생성
    teams = [
        Team(id="T01", name="사업PMO팀"),
        Team(id="T02", name="전략사업팀"),
        Team(id="T03", name="그룹사업팀"),
        Team(id="T04", name="전략개발팀")
    ]
    session.add_all(teams)

    members = [
        Member(id="82022284", name="윤주형", position="M4", team_id="T04"),
        Member(id="82022285", name="최병윤", position="M4", team_id="T04"),
        Member(id="82022286", name="권성광", position="M3", team_id="T04"),
        Member(id="82022287", name="김하성", position="M2", team_id="T04"),
        Member(id="82022288", name="이명진", position="M2", team_id="T04"),
        Member(id="82022289", name="김홍기", position="M2", team_id="T04"),
        Member(id="82022290", name="신해빈", position="M2", team_id="T04"),
        Member(id="89999991", name="이지현", position="M5", team_id="T01"),
        Member(id="99999992", name="양나라", position="M5", team_id="T02"),
        Member(id="99999993", name="박찬수", position="M5", team_id="T03"),
    ]
    session.add_all(members)

    projects = [
        Project(name="하나은행", start_date=datetime.strptime("2024-01-01", "%Y-%m-%d"), 
                end_date=datetime.strptime("2024-12-31", "%Y-%m-%d")),
        Project(name="미래에셋", start_date=datetime.strptime("2024-01-01", "%Y-%m-%d"), 
                end_date=datetime.strptime("2024-12-31", "%Y-%m-%d")),
        Project(name="한신평", start_date=datetime.strptime("2024-01-01", "%Y-%m-%d"), 
                end_date=datetime.strptime("2024-12-31", "%Y-%m-%d")),
        Project(name="교육청", start_date=datetime.strptime("2024-01-01", "%Y-%m-%d"), 
                end_date=datetime.strptime("2024-12-31", "%Y-%m-%d")),
    ]
    session.add_all(projects)

    users = [
        User(name="관리자", email="rms@kt.com"),
    ]
    session.add_all(users)

    session.commit()

def insert_test_data2(session: Session):
    project1: Project = session.query(Project).filter(Project.name == '하나은행').first()
    print(vars(project1))

    member1 = session.query(Member).filter(Member.name == '권성광').first()
    project_member = ProjectMember(project=project1, member=member1, start_date=datetime.now(), end_date=datetime.now())
    session.add(project_member)

session = SessionLocal()
insert_test_data(session)
insert_test_data2(session)
