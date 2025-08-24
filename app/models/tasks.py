from sqlalchemy import Integer, String
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
