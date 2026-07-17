from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db, Base, engine
from routers.classrooms import router as classrooms_router
from routers.students import router as students_router

app = FastAPI()

Base.metadata.create_all(bind = engine)

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

app.include_router(classrooms_router)
app.include_router(students_router)