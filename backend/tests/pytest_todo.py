import pytest
from sqlalchemy.orm import Session
from database import Base, TestSessionLocal, test_engine
from models import User

@pytest.fixture(scope="function")
def db_session():
    # 데이터베이스 초기화
    Base.metadata.create_all(bind=test_engine)
    db = TestSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture(scope="function")
def insert_test_data(db_session: Session):
    # 테스트 데이터 삽입
    users = [
        User(name="Alice", email="alice@example.com"),
        User(name="Bob", email="bob@example.com"),
    ]
    db_session.add_all(users)
    db_session.commit()
    yield