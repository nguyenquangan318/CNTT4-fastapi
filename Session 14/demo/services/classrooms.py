from sqlalchemy.orm import Session
from models.classrooms import ClassroomModel
from schemas.classrooms import CreateClass, UpdateClass

def get_all_classes_service(db: Session):
    list_classes = db.query(ClassroomModel).all()
    return list_classes

def get_class_by_id_service(db:Session, id: int):
    classroom = db.query(ClassroomModel).filter(ClassroomModel.id == id).first()
    return classroom

def create_class_service(db:Session, new_class: CreateClass):
    classroom = ClassroomModel(**new_class.model_dump())
    db.add(classroom)
    db.commit()
    db.refresh(classroom)
    return classroom

def update_class_service(db:Session, update_class: UpdateClass, id:int):
    class_in_db = db.query(ClassroomModel).filter(ClassroomModel.id == id).first()
    if class_in_db is None:
        return class_in_db
    for key, value in update_class.model_dump().items():
        setattr(class_in_db, key, value)
    db.commit()
    db.refresh(class_in_db)
    return class_in_db

def delete_class_service(db:Session, id: int):
    class_in_db = db.query(ClassroomModel).filter(ClassroomModel.id == id).first()
    delete_class = class_in_db
    if class_in_db is None:
        return class_in_db
    db.delete(class_in_db)
    db.commit()
    return delete_class