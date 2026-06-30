from fastapi import FastAPI

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

app = FastAPI()

@app.get('/courses')
def get_courses():
    return {
        "data": courses
    }
    
@app.get('/course/testcourse')
def get_test_course():
    pass
# /course/1 
@app.get('/course/{course_id}')
def get_course_by_id(course_id):
    for course in courses:
        if course_id == str(course['id']):
            return {
                "message": "Tìm thấy lớp học",
                "data": course
            }
    return {
        "message": "Không tìm thấy lớp học",
        "data": None
    }

