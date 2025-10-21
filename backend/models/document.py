from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    file_path = Column(String)
    title = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
