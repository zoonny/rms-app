from sqlalchemy import MetaData, inspect
from db.database import Base, engine

inspector = inspect(engine)
tables = inspector.get_table_names()
print("Existing tables:", tables)

# 특정 테이블이 존재하는지 확인
if "my_table" in tables:
    print("Table exists!")

Base.metadata.reflect(bind=engine)  # 데이터베이스에서 현재 테이블 정보를 가져옴

# 현재 메타데이터에 등록된 테이블 확인
# print(MetaData().tables.keys())

# 테이블 삭제
Base.metadata.drop_all(engine)