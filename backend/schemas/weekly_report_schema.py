from pydantic import ConfigDict, BaseModel
from datetime import date

class WeeklyReportBase(BaseModel):
    week_number: int
    base_date: date
    this_week: str
    next_week: str

class WeeklyReportCreate(WeeklyReportBase):
    pass

class WeeklyReportUpdate(WeeklyReportBase):
    pass

class WeeklyReportResponse(WeeklyReportBase):
    id: int

    model_config = ConfigDict(from_attributes=True)