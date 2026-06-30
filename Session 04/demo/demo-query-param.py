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

# /courses?start_price=2000000&end_price=4500000
@app.get('/courses')
def get_courses(start_price: float, end_price: float = 4000000):
    filter_courses = []
    for course in courses:
        if start_price <= course['price'] <= end_price:
            filter_courses.append(course)
    if filter_courses:
        return {
            "message": "Lọc được danh sách khóa học trong khoảng giá",
            "data": filter_courses
        }
    return {
        "message": "Không có khóa học trong khoảng giá",
        "data": None
    }
