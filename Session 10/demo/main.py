from fastapi import FastAPI, Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel
from datetime import datetime
from classroom_services import create_class_service, get_all_class_service, get_class_by_id_service

app = FastAPI()

class CreateClass(BaseModel):
    class_code: str
    name: str
    description: str
    created_at: datetime

@app.get('/test_connection')
def test_db_connect(db:Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return {
            "status": "Success!",
            "message": "Kết nối thành công"
        }
    except Exception as err:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(err))
    
@app.post('/classroom', status_code=status.HTTP_201_CREATED)
def create_class(new_class: CreateClass, db:Session = Depends(get_db)):
    new_class = create_class_service(db, new_class.class_code, new_class.name, new_class.description, new_class.created_at)
    return {
        "message": "Success!",
        "data": new_class
    }
    
@app.get('/classrooms')
def get_all_class(db:Session = Depends(get_db)):
    list_classes = get_all_class_service(db)
    return {
        "message": "Success!",
        "data": list_classes
    }
    
@app.get('/classroom/{id}')
def get_class_by_id(id: int, db:Session = Depends(get_db)):
    classroom = get_class_by_id_service(db, id)
    if classroom is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Lớp không tồn tại")
    return {
        "message": "Success!",
        "data": classroom
    }