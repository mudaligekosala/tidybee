import enum
from sqlalchemy import Integer, String, Enum
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class TaskType(enum.Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    type: Mapped[TaskType] = mapped_column(Enum(TaskType),nullable=False, index=True)
