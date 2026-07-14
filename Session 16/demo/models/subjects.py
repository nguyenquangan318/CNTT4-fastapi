from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.student_subject import student_subject

# Bảng môn học có id, name
class SubjectModel(Base):
    __tablename__ = "subjects"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    
    students = relationship(
        "StudentModel",
        back_populates="subjects",
        secondary = student_subject
    )
    