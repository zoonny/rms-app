# PostgreSQL 공식 이미지를 사용
FROM postgres:15

# 환경 변수 설정
ENV POSTGRES_USER=stgbsuser
ENV POSTGRES_PASSWORD=sideV1234!
ENV POSTGRES_DB=stgbsdb

# 초기화 스크립트를 복사 (선택 사항)
# 컨테이너 시작 시 실행될 SQL 파일이나 Shell 스크립트를 복사
COPY ./init-scripts /docker-entrypoint-initdb.d/

# PostgreSQL이 기본적으로 5432 포트를 사용
EXPOSE 5432
