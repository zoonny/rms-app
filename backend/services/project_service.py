from sqlalchemy.orm import Session
from crud.project_crud import ProjectCRUD
from schemas.project_schema import ProjectCreate, ProjectUpdate

class ProjectService:
    def __init__(self, db: Session, crud: ProjectCRUD):
        self.db = db
        self.crud = crud

    def list_projects(self, skip: int = 0, limit: int = 10):
        return self.crud.get_projects(self.db, skip=skip, limit=limit)

    def get_project(self, project_id: int):
        project = self.crud.get_project(self.db, project_id=project_id)
        if not project:
            raise ValueError("Project not found")
        return project 

    def create_project(self, project: ProjectCreate):
        return self.crud.create_project(self.db, project=project)

    def update_project(self, project_id: int, project: ProjectUpdate):
        return self.crud.update_project(self.db, project_id=project_id, project=project)

    def delete_project(self, project_id: int):
        return self.crud.delete_project(self.db, project_id=project_id)