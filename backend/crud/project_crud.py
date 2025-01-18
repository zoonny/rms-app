from sqlalchemy.orm import Session
from models.project import Project
from schemas.project_schema import ProjectCreate, ProjectUpdate

class ProjectCRUD:
    def get_projects(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Project).offset(skip).limit(limit).all()
        # projects = db.query(Project).offset(skip).limit(limit).all()
        # print(projects)
        # return projects

    def get_project(self, db: Session, project_id: int):
        return db.query(Project).filter(Project.id == project_id).first()

    def create_project(self, db: Session, project: ProjectCreate):
        db_project = project.to_model()
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

    def update_project(self, db: Session, project_id: int, project: ProjectUpdate):
        db_project = db.query(Project).filter(Project.id == project_id).first()
        if db_project:
            project.update_model(db_project)
            db.commit()
            db.refresh(db_project)
        return db_project

    def delete_project(self, db: Session, project_id: int):
        db_project = db.query(Project).filter(Project.id == project_id).first()
        if db_project:
            db.delete(db_project)
            db.commit()
        return db_project