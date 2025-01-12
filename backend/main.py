import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from db.database import Base, engine
from api import user_router, project_router, member_router, weekly_report_router, team_router, auth_router

# 데이터베이스 초기화
Base.metadata.create_all(bind=engine)

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="RMS APP",
    description="Resource Management Service Application",
    version="0.1.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/api/openapi.json",
)

app.swagger_ui_parameters = {
    "docExpansion": "none",             # 기본적으로 모든 경로를 닫기
    # "defaultModelsExpandDepth": -1,   # 모델(Schemas) 섹션 숨기기
}

# CORS 설정
origins = [
    "http://localhost:8000",
    "http://localhost:8100",
    "http://0.0.0.0:8100",
    # 추가로 허용할 도메인들을 여기에 나열
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Referrer-Policy 설정을 위한 미들웨어
class ReferrerPolicyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        return response

app.add_middleware(ReferrerPolicyMiddleware)

# 라우터 등록
app.include_router(team_router.router, prefix="/api", tags=["team"])
app.include_router(member_router.router, prefix="/api", tags=["members"])
app.include_router(project_router.router, prefix="/api", tags=["projects"])
app.include_router(weekly_report_router.router, prefix="/api", tags=["weekly_report"])
app.include_router(user_router.router, prefix="/api", tags=["users"])
app.include_router(auth_router.router, prefix="/api", tags=["auth"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)