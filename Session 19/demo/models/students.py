from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.student_subject import student_subject

# Bảng sinh viên có id, name, age
class StudentModel(Base):
    __tablename__ = "students"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    classroom_id = Column(Integer, ForeignKey("classes.id"))
    
    classroom = relationship(
        "ClassroomModel",
        back_populates="students",
        uselist=False
    )
    
    subjects = relationship(
        "SubjectModel",
        back_populates="students",
        secondary = student_subject
    )