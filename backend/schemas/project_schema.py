from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProjectBase(BaseModel):
    name: str
    start_time: datetime
    end_time: datetime

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int

    model_config = ConfigDict(from_attributes=True)