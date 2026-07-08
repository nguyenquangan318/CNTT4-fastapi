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