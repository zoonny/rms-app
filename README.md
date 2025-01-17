# RMS-APP

#### git 저장

```shell
git config --global user.name "zoonny"
git config --global user.email "hyungii@naver.com"
cd /home/azureuser/app/rms-app
git init
# github repository 생성
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/zoonny/rms-app.git
git branch -M main
git push -u origin main
git push origin main --force
```

#### container dev

```shell
docker build -f Dockerfile.dev -t rms-app-dev .
docker run -d -t --name rms-app-dev -v ${PWD}:/app -p 8000:8000 rms-app-dev
# -t 실행 상태 유지

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

```shell
docker build -t rms-db .
docker run -d --name rms-db-container -p 5432:5432 rms-db
```

#### 실행

```shell
docker build -t rms-app .
docker run -d -p 8000:80 rms-app

# curl http://localhost:8080/api/users
# curl http://localhost:8000/api/users
# http://52.231.105.193:8080/docs

docker stop $(docker ps -a | grep rms-app | awk '{print$1}')
docker rm $(docker ps -a | grep rms-app | awk '{print$1}')
docker logs --tail 10 -f $(docker ps -a | grep rms-app | awk '{print$1}')
docker exec -it $(docker ps -a | grep rms-app | awk '{print$1}') /bin/bash

docker logs --tail 10 -f <container id>
docker exec -it 10e4d44748a3 /bin/bash
uvicorn main:app --host 0.0.0.0 --port 8080

docker login -u hyungii@naver.com
1h*****35
docker tag rms-app hyungii/rms-app:0.1
# azureuser@sidev-k8s-master1:~/app/rms-app$ docker images
# REPOSITORY        TAG       IMAGE ID       CREATED              SIZE
# hyungii/rms-app   0.1       56f108a8f9f4   About a minute ago   180MB
# rms-app           latest    56f108a8f9f4   About a minute ago   180MB
docker push hyungii/rms-app:0.1
```

```shell
# PV: 스토리지 제공 리소스
# PVC: 애플리케이션이 PV를 요청하고 사용하는 리소스
kubectl apply -f pv.yaml
azureuser@sidev-k8s-master1:~/app$ kg pv -o wide
# NAME     CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE   VOLUMEMODE
# app-pv   2Gi        RWO            Retain           Available                          <unset>                          15m   Filesystem
```

```shell
kubectl apply -f postgres-deployment.yaml
# azureuser@sidev-k8s-master1:~/app/rms-app$ kubectl apply -f postgres-deployment.yaml 
# persistentvolumeclaim/postgres-pvc created
# deployment.apps/postgres-deployment created
# service/postgres-service created

kubectl apply -f rms-app-deployment.yaml

kg deployment -o wide
kg svc -o wide
kg pvc -o wide

kubectl delete -f rms-app-deployment.yaml
```

fastapi_crud/
├── main.py              # FastAPI 엔트리 포인트
├── models.py            # SQLAlchemy 모델 정의
├── schemas.py           # Pydantic 스키마 정의
├── database.py          # 데이터베이스 설정
├── crud.py              # CRUD 로직 구현
├── routers/
│   ├── user_router.py   # User 관련 API 라우트 정의
└── requirements.txt     # 필요한 패키지 목록


http://127.0.0.1:8000/docs


### frontend

shadcn/ui

```shell
# nextjs 프로젝트 생성
npx shadcn@latest init
# 프로젝트 이름 입력: rms-app
# 스타일 선택: Default
# 스타일 기본 색상: Slate
# React Server Components 사용 여부: yes
# Tailwind CSS 설정 파일 경로: tailwind.config.js
# CSS 글로벌 스타일 파일 경로: app/globals.css
# components 디렉토리 경로: components
# utils.ts 파일 경로: lib/utils.ts
# React 18 사용 여부: yes
# TypeScript 사용 여부: yes
# ESLint 사용 여부: yes
# Prettier 사용 여부: yes
# Import alias 설정: yes (@/components)
npx shadcn@latest add button
npx shadcn@latest add sidebar
npx shadcn@latest add dropdown-menu
npx shadcn@latest add collapsible
npx shadcn@latest add avatar

npm run dev
```
