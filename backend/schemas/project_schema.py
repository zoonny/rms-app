from pydantic import BaseModel, ConfigDict
from models.project import Project
from datetime import datetime

class ProjectBase(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime

class ProjectCreate(ProjectBase):
    def to_model(self):
        project = Project(
            name=self.name,
            start_date=self.start_date,
            end_date=self.end_date)
        return project
    pass

class ProjectUpdate(ProjectBase):
    def update_model(self, project: Project):
        project.name = self.name
        project.start_date = self.start_date
        project.end_date = self.end_date
        return
    pass

class ProjectResponse(ProjectBase):
    id: int

    model_config = ConfigDict(from_attributes=True)