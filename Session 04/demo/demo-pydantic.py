from fastapi import FastAPI
from pydantic import BaseModel, Field

courses = [
    {
        "id": 1,
        "name": "Python Basic",
        "category": "backend",
        "price": 3000000,
        "mode": "online"
    },
    {
        "id": 2,
        "name": "Java Web",
        "category": "backend",
        "price": 5000000,
        "mode": "offline"
    },
    {
        "id": 3,
        "name": "Web Frontend",
        "category": "frontend",
        "price": 4000000,
        "mode": "online"
    }
]

class CreateCourse(BaseModel):
    id: int
    name: str = Field(min_length=2)
    category: str
    price: float = Field(ge=0, le=1000000000)
    mode: str

app = FastAPI()

@app.post('/course')
def create_course(course: CreateCourse):
    courses.append({
            "id": course.id,
            "name": course.name,
            "price": course.price,
            "category": course.category,
            "mode": course.mode,
        })
    return{
        "message": "Thêm khóa học thành công",
        "data": courses
    }
