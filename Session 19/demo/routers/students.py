from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from services.students import add_subjects_service

router = APIRouter(prefix='/students', tags=['students'])

# Viết endpoint API đăng ký môn học cho sinh viên
@router.put('/{id}/subjects')
def add_subjects(id:int, subjects: list[int], db:Session = Depends(get_db)):
    student = add_subjects_service(db, id, subjects)
    return student
        