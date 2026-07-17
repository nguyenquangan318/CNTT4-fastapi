from sqlalchemy.orm import Session, joinedload
from models.students import StudentModel
from models.subjects import SubjectModel

# Viết logic API đăng ký môn học cho sinh viên
def add_subjects_service(db: Session, id: int, subjects: list[int]):
    db_student = db.query(StudentModel).filter(StudentModel.id == id).options(
        joinedload(StudentModel.subjects)    
    ).first()
    if db_student is None:
        return "sinh viên không tồn tại"
    db_subjects = db.query(SubjectModel).filter(SubjectModel.id.in_(subjects)).all()
    db_student.subjects = db_subjects
    db.commit()
    db.refresh(db_student)
    return db_student