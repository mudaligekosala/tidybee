from pydantic import BaseModel, Field

from app.models.tasks import TaskType

class TaskBase(BaseModel):
    name:str
    type:TaskType

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id:int

    class Config:
        orm_mode = True


