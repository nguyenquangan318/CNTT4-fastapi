from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from classroom_services import delete_class_service, update_class_service, create_class_service, get_all_classes_service, get_class_by_id_service
from schemas import CreateClass, UpdateClass

app = FastAPI()

@app.get('/test-connection')
def test_connect(db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return{
            "messsage": "Success!"
        }
    except Exception as err:
        return {
            "messsage": str(err)
        }
        
@app.get('/classrooms')
def get_all_classes(db: Session = Depends(get_db)):
    list_classes = get_all_classes_service(db)
    return {
        "message": "Success!",
        "data": list_classes
    }
    
@app.get("/classroom/{id}")
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
    
@app.post('/classroom')
def create_class(new_class: CreateClass, db: Session = Depends(get_db)):
    classroom = create_class_service(db, new_class)
    return {
        "message": "Success!",
        "data": classroom
    }
    
@app.put('/classroom/{id}')
def create_class(id:int, update_class: UpdateClass, db: Session = Depends(get_db)):
    classroom = update_class_service(db, update_class, id)
    return {
        "message": "Success!",
        "data": classroom
    }
    
@app.delete('/classroom/{id}')
def delete_class(id:int, db: Session = Depends(get_db)):
    classroom = delete_class_service(db, id)
    return {
        "message": "Success!",
        "data": classroom
    }