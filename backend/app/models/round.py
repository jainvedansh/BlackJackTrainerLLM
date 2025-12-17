from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)

    # one session -> many rounds
    rounds = relationship("Round", back_populates="session")


class Round(Base):
    __tablename__ = "rounds"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)

    # many rounds -> one session
    session = relationship("Session", back_populates="rounds")

    state = Column(String, nullable=False)
    bet_amount = Column(Integer, nullable=False)
    outcome = Column(String, nullable=True)

    start_time = Column(DateTime, default=datetime.utcnow)
