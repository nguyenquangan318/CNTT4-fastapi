from pydantic import BaseModel
from datetime import datetime

class CreateClass(BaseModel):
    class_code: str
    name: str
    description: str
    created_at: datetime

class UpdateClass(BaseModel):
    class_code: str
    name: str
    description: str
    
class StudentResponseInClass(BaseModel):
    id: int
    name: str
    age: int

class TeacherResponseInClass(BaseModel):
    id: int
    name: str
    age: int
 
class FullClassResponse(BaseModel):
    id: int
    class_code: str
    name: str
    description: str
    created_at: datetime
    students: list[StudentResponseInClass]
    teacher: TeacherResponseInClass
    
