from fastapi import FastAPI, Request, status, HTTPException
from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

carriers = [
    {"id": 1, "code": "GHN", "name": "Giao Hang Nhanh", "max_weight_capacity": 5000, "status": "ACTIVE"},
    {"id": 2, "code": "GHTK", "name": "Giao Hang Tiet Kiem", "max_weight_capacity": 3000, "status": "ACTIVE"},
    {"id": 3, "code": "VTP", "name": "Viettel Post", "max_weight_capacity": 10000, "status": "SUSPENDED"}
]
shipments = [
    {
        "id": 1,
        "carrier_id": 1,
        "order_reference": "ORD-2026-001",
        "total_weight": 4200,
        "dispatch_date": "2026-07-01",
        "shift": "MORNING"
    }
]

app = FastAPI()

class BaseResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any]
    errors: Optional[Any]
    timestamp: str
    path: str
    
class CreateCarrie(BaseModel):
    id: int
    code: str
    name: str
    max_weight_capacity: int
    status: str
    
def create_response(req: Request, status_code: int, message: str, data = None, errors = None):
    return BaseResponse(
        status_code = status_code,
        message = message,
        data = data,
        errors = errors,
        timestamp = datetime.now().isoformat(),
        path = req.url.path
    )

@app.get('/carries')
def get_carries(request: Request):
    return create_response(request, status.HTTP_200_OK, "Success!", carriers)

@app.get('/carrie/{id}')
def get_carrie_by_id(request: Request, id: int):
    for c in carriers:
        if c['id'] == id:
            return create_response(request, status.HTTP_200_OK, "Success!", c)
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Đối tác không tồn tại")

@app.post('/carrie', status_code=status.HTTP_201_CREATED)
def create_carrie(request: Request, new_carrie: CreateCarrie):
    new_carrie = {
        "id": new_carrie.id,
        "code":new_carrie.code, 
        "name": new_carrie.name, 
        "max_weight_capacity": new_carrie.max_weight_capacity, 
        "status": new_carrie.status 
    }
    carriers.append(new_carrie)
    return create_response(request, status.HTTP_201_CREATED, "Success!", new_carrie)

@app.exception_handler(Exception)
def global_exception_handle(
    request: Request,
    exc: Exception
):
    response = create_response(request, status.HTTP_500_INTERNAL_SERVER_ERROR, "Failed!", errors = str(exc))
    return JSONResponse(
        content = response.model_dump(),
        status_code = response.status_code
    )

@app.exception_handler(HTTPException)
def global_exception_handle(
    request: Request,
    exc: HTTPException
):
    response = create_response(request, exc.status_code, "Failed!", errors = exc.detail)
    return JSONResponse(
        content = response.model_dump(),
        status_code = response.status_code
    )
    

@app.exception_handler(RequestValidationError)
def global_exception_handle(
    request: Request,
    exc: RequestValidationError
):
    response = create_response(request, status.HTTP_422_UNPROCESSABLE_CONTENT, "Failed!", errors = exc.errors())
    return JSONResponse(
        content = response.model_dump(),
        status_code = response.status_code
    )