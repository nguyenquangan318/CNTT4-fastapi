from database import Base
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

# Bảng phụ liên kết sinh viên và môn học
student_subject = Table(
    "student_subject",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subjects.id"), primary_key=True)
)

