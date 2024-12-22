from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.project_schema import ProjectCreate, ProjectUpdate, ProjectResponse
from db.database import get_db
from services.project_service import ProjectService
from crud.project_crud import ProjectCRUD

router = APIRouter()

def get_project_service(db: Session = Depends(get_db)):
    crud = ProjectCRUD()
    return ProjectService(db=db, crud=crud)

@router.get("/projects", response_model=list[ProjectResponse])
def read_projects(skip: int = 0, limit: int = 10, project_service: ProjectService = Depends(get_project_service)):
    return project_service.list_projects(skip=skip, limit=limit)

@router.get("/projects/{project_id}", response_model=ProjectResponse)
def read_project(project_id: int, project_service: ProjectService = Depends(get_project_service)):
    try:
        return project_service.get_project(project_id=project_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/projects", response_model=ProjectResponse)
def create_new_project(project: ProjectCreate, project_service: ProjectService = Depends(get_project_service)):
    try:
        return project_service.create_project(project=project)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/projects/{project_id}", response_model=ProjectResponse)
def update_existing_project(project_id: int, project: ProjectUpdate, project_service: ProjectService = Depends(get_project_service)):
    try:
        return project_service.update_project(project_id, project)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/projects/{project_id}")
def delete_existing_project(project_id: int, project_service: ProjectService = Depends(get_project_service)):
    try:
        return project_service.delete_project(project_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))