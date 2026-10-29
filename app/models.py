from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String
from app.database import Base

from datetime import datetime

class Lesson(Base):
    __tablename__ = "Lesson"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )
    end_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )