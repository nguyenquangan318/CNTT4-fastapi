from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from services.classrooms import delete_class_service, update_class_service, create_class_service, get_all_classes_service, get_class_by_id_service
from schemas.classrooms import CreateClass, UpdateClass

router = APIRouter(prefix='/classrooms', tags=['classrooms'])
        
@router.get('/')
def get_all_classes(db: Session = Depends(get_db)):
    list_classes = get_all_classes_service(db)
    return {
        "message": "Success!",
        "data": list_classes
    }
    
@router.get("/{id}")
def get_class_by_id(id:int, db: Session = Depends(get_db)):
    classroom = get_class_by_id_service(db, id)
    if classroom is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "Lop khong ton tai"
        )
    return{
        "message": "Success!",
        "data": classroom
    }
    
@router.post('/')
def create_class(new_class: CreateClass, db: Session = Depends(get_db)):
    classroom = create_class_service(db, new_class)
    return {
        "message": "Success!",
        "data": classroom
    }
    
@router.put('/{id}')
def create_class(id:int, update_class: UpdateClass, db: Session = Depends(get_db)):
    classroom = update_class_service(db, update_class, id)
    return {
        "message": "Success!",
        "data": classroom
    }
    
@router.delete('/{id}')
def delete_class(id:int, db: Session = Depends(get_db)):
    classroom = delete_class_service(db, id)
    return {
        "message": "Success!",
        "data": classroom
    }