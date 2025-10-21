from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String, default="citizen")
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    chats = relationship("Chat", back_populates="user", cascade="all, delete-orphan")
    notebooks = relationship("Notebook", back_populates="user", cascade="all, delete-orphan")
