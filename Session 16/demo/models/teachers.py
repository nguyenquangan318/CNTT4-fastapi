from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Bảng giảng viên chủ nhiệm có id, name, age
class TeacherModel(Base):
    __tablename__ = "teachers"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    classroom_id = Column(Integer, ForeignKey("classes.id"), unique=True)
    
    classroom = relationship(
        "ClassroomModel",
        back_populates="teachers",
        uselist=False
    )
    
# teacher = TeacherModel()
# classroom = ClassroomModel()
# print(teacher.classroom)
# teacher.classroom = classroom
# print(teacher.classroom)
# print(classroom.teacher)