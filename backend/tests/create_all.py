from sqlalchemy import text, inspect
from db.database import Base, engine
# 생성을 위한 모델 import
# from models.member import Member
# from models.project import Project
# from models.team import Team
# from models.user import User
# from models.weekly_report import WeeklyReport
from models import Member, Project, Team, User, WeeklyReport

# 테이블 생성
Base.metadata.create_all(engine)

inspector = inspect(engine)
tables = inspector.get_table_names()
print("Existing tables:", tables)