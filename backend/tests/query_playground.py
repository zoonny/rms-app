from sqlalchemy import or_, func, text
from sqlalchemy.orm import Session
from pprint import pprint
from db.database import SessionLocal
from models import Member, Project, Team, User, WeeklyReport, ProjectMember, Permission
from datetime import datetime, date

session = SessionLocal()

def selectAll():
    members: list[Member] = session.query(Member).all()
    for member in members:
        print(member.id, member.name)
        # pprint(vars(member))

def selectOne():
    member: Member = session.query(Member).filter(Member.name == '윤주형').first()
    print(member.id, member.name)

def selectAnd():
    member: Member = session.query(Member).filter(Member.id == '82022284', Member.name == '윤주형').first()
    if member:
        print(member.id, member.name)

def selectOr():
    members: list[Member] = session.query(Member).filter(or_(Member.id == '82022284', Member.name == '이명진')).all()
    for member in members:
        print(member.id, member.name)

def selectOrderBy():
    members: list[Member] = session.query(Member).order_by(Member.name).all()
    for member in members:
        print(member.id, member.name)

    print('--------------------------')

    members: list[Member] = session.query(Member).order_by(Member.name.desc()).all()
    for member in members:
        print(member.id, member.name)

def selectLimitOffset():
    members: list[Member] = session.query(Member).limit(5).all()
    for member in members:
        print(member.id, member.name)

    print('--------------------------')

    members: list[Member] = session.query(Member).offset(4).limit(5).all()
    for member in members:
        print(member.id, member.name)

def selectColumn():
    members: list[Member] = session.query(Member.id, Member.name).all()
    for member in members:
        print(member.id, member.name)

def selectCount():
    count: int = session.query(func.count(Member.id)).scalar()
    print(f'Total members: {count}')

def selectInnerJoin():
    results = session.query(Member, Team).join(Team.members).all()
    for member, team in results:
        print(member.name, team.name)

# def selectOuterJoin():
#     results = session.query(Member, ProjectMember).outerjoin(Project.member_links).all()
#     for member, project_member in results:
#         print(member.name, project_member.project_id if project_member else "No project")

# def selectSubquery():
#     subquery = session.query(Member.id).filter(Member.id == '82022284').subquery()
#     projects = session.query(Team).filter(Team.id.in_(subquery)).all()
#     for project in projects:
#         print(project.name)

def selectCountBySql(team_id: str = 'T004'):
    sql = text("SELECT * FROM member WHERE team_id > :team_id")
    members = session.execute(sql, {"team_id": team_id})
    session.commit()
    print(f"{team_id}: {members}")

def updateMemberName():
    session.query(Member).filter(Member.id == '82022284').update({Member.name: 'Updated'})
    session.commit()

    member: Member = session.query(Member).filter(Member.id == '82022284').first()
    print(f'id:{member.id} name:{member.name}')

    session.query(Member).filter(Member.id == '82022284').update({Member.name: '윤주형'})
    session.commit()

    member: Member = session.query(Member).filter(Member.id == '82022284').first()
    print(f'id:{member.id} name:{member.name}')

def deleteMember(member_id: str):
    session.query(Member).filter(Member.id == member_id).delete()
    session.commit()

    # member: Member = session.query(Member).filter(Member.id == member_id).first()
    # if member:
    #     print(f'id:{member.id} name:{member.name}')
    # else:
    #     print(f'No member')

def insertMemberByOrm():
    new_member = Member(id="1", employee_id="1", name="테스트", position="M0", team_id="T01")
    session.add(new_member)
    session.commit()

    member = session.query(Member).filter(Member.id == '1').first()
    print(f"name: {member.name}")

    members = [
        Member(id="2", employee_id="2", name="테스트2", position="M0", team_id="T01"),
        Member(id="3", employee_id="3", name="테스트3", position="M0", team_id="T01")
    ]
    session.add_all(members)
    session.commit()

    selectAll()

    deleteMember("1")
    deleteMember("2")
    deleteMember("3")

    selectAll()

def insertMemberByCore():
    pass

def insertMemberBySql():
    pass

def insertManyToMany():
    read_permission = Permission(name="read")
    write_permission = Permission(name="write")

    user1 = User(name="사용자1", email="user1@kt.com")
    user2 = User(name="사용자2", email="user2@kt.com")

    user1.permissions.append(read_permission)
    user1.permissions.append(write_permission)
    user2.permissions.append(read_permission)

    session.add_all([user1, user2])
    session.commit()

def selectManyToMany():
    user1 = session.query(User).filter(User.name == '사용자1').first()
    print([perm.name for perm in user1.permissions])

    read_perm = session.query(Permission).filter_by(name='read').first()
    print([user.name for user in read_perm.users])

def insertPermission():
    admin_user = session.query(User).filter_by(name='관리자').first()
    print(f'name: {admin_user.name}')

    read_perm = session.query(Permission).filter_by(name='read').first()
    admin_user.permissions.append(read_perm)

    session.commit()

def get_member_count(db: Session, team_id: str):
    # return db.query(Member).filter(Member.team_id == team_id).count()
    count = db.query(Member).filter(Member.team_id == team_id).count()
    print(count)

def get_member_project_and_weeklyReport(db: Session, member_id: str):
    member = db.query(Member).filter(Member.id == member_id).first()
    pprint('==> member')
    pprint(vars(member))
    pprint('==> team')
    pprint(vars(member.team))
    pprint('==> weekly_report')
    pprint([(weekly_report.id, weekly_report.base_date) for weekly_report in member.weekly_reports])

def get_member_task(db: Session, member_id: str):
    member = db.query(Member).filter(Member.id == member_id).first()
    pprint('==> member')
    pprint(vars(member))
    pprint('==> task')
    pprint(vars(member.task_links[0].task))

def get_member_task2(db: Session, member_id: str):
    member = db.query(Member).filter(Member.id == member_id).first()
    pprint('==> member')
    pprint(vars(member))
    pprint('==> task')
    pprint(vars(member.tasks[0]))

# selectAll()
# selectOne()
# selectAnd()
# selectOr()
# selectOrderBy()
# selectLimitOffset()
# selectColumn()
# selectCount()
# selectInnerJoin()
# selectOuterJoin()
# selectCountBySql()
# selectSubquery()
# updateMemberName()
# deleteMember("1")
# insertMemberByOrm()
# insertMemberByCore()
# insertMemberBySql()
# insertManyToMany()
# selectManyToMany()
# insertPermission()
# get_member_count(db=session, team_id="T04")
# get_member_project_and_weeklyReport(db=session, member_id='82022284')
# get_member_task(db=session, member_id='82022284')
get_member_task2(db=session, member_id='82022284')
