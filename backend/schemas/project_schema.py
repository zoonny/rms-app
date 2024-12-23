from pydantic import BaseModel, ConfigDict
from models.project import Project
from datetime import datetime

class ProjectBase(BaseModel):
    name: str
    start_time: datetime
    end_time: datetime

class ProjectCreate(ProjectBase):
    def to_model(self):
        project = Project(
            name=self.name,
            start_time=self.start_time,
            end_time=self.end_time)
        return project
    pass

class ProjectUpdate(ProjectBase):
    def update_model(self, project: Project):
        project.name = self.name
        project.start_time = self.start_time
        project.end_time = self.end_time
        return
    pass

class ProjectResponse(ProjectBase):
    id: int

    model_config = ConfigDict(from_attributes=True)