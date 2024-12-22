from fastapi import FastAPI
from db.database import Base, engine
from api import user_router

# 데이터베이스 초기화
Base.metadata.create_all(bind=engine)

# FastAPI 애플리케이션 생성
app = FastAPI()

# 라우터 등록
app.include_router(user_router.router, prefix="/api", tags=["users"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)