from sqlalchemy import text
from db.database import SessionLocal

# [ERROR] ModuleNotFoundError: No module named 'db' 발생 시 아래 수행
# export PYTHONPATH=$PYTHONPATH:/app

# 세션 생성
session = SessionLocal()

# 데이터 조회
result = session.execute(text("SELECT * FROM users WHERE name = :name"), {"name": "string"})
for row in result:
    print(row)