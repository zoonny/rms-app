from sqlalchemy.orm import Session
from models.project import Project
from schemas.project_schema import ProjectCreate, ProjectUpdate

class ProjectCRUD:
    def get_projects(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Project).offset(skip).limit(limit).all()

    def get_project(self, db: Session, project_id: int):
        return db.query(Project).filter(Project.id == project_id).first()

    def create_project(self, db: Session, project: ProjectCreate):
        db_project = Project(name=project.name, start_time=project.start_time, end_time=project.end_time)
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

    def update_project(self, db: Session, project_id: int, project: ProjectUpdate):
        db_project = db.query(Project).filter(Project.id == project_id).first()
        if db_project:
            db_project.name = project.name
            db_project.start_time = project.start_time
            db_project.end_time = project.end_time
            db.commit()
            db.refresh(db_project)
        return db_project

    def delete_project(self, db: Session, project_id: int):
        db_project = db.query(Project).filter(Project.id == project_id).first()
        if db_project:
            db.delete(db_project)
            db.commit()
        return db_project