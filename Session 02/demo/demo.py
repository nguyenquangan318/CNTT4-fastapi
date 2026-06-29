# import fastapi
from fastapi import FastAPI

# Tạo thực thể
app = FastAPI()

# Tạo API
@app.get('/')
def get_root():
    result = 5 + 5
    return result

@app.get('/student')
def get_student():
    return {
        "id": 1,
        "fullName" : 'Nguyễn Văn A'
    }