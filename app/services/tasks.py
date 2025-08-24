from sqlalchemy.exc import IntegrityError
from app.models.tasks import TaskType
from app.session import session_scope
from models import Tasks

class TaskAlreadyExistsError(Exception):
    """Raised when attempting to add task with same name"""

class TaskNotFoundError(Exception):
    """Raised when a requested task not found"""

def createTask(*, name:str, type: TaskType) -> Tasks:
    with session_scope() as db:
        task = Tasks(name, type)
        db.add(task)
        try:
            pass
        except IntegrityError as e:
            raise TaskAlreadyExistsError from e
        
    return task

