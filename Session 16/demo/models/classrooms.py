from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.teachers import TeacherModel
from models.students import StudentModel
from models.subjects import SubjectModel

class ClassroomModel(Base):
    __tablename__ = "classes"
    id = Column(Integer, autoincrement=True, primary_key=True)
    class_code = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)

    teacher = relationship(
        "TeacherModel",
        back_populates="classes",
        uselist=False
    )
    
    students = relationship(
        "StudentModel",
        back_populates="classes"
    )