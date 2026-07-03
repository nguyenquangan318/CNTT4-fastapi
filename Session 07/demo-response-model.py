from fastapi import FastAPI, status, Request, HTTPException
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Any
from fastapi.responses import JSONResponse

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000},
    {"id": 3, "name": "Screen", "price": 400000}
]

class BaseResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any]
    error: Optional[str]
    timestamp: str
    path: str
    
def create_response(request ,status_code :int, message: str, data = None, error = None):
    response = BaseResponse(
        status_code = status_code,
        message = message,
        data = data,
        error = error,
        timestamp = datetime.now().isoformat(),
        path = request.url.path
    )
    return response

app = FastAPI()

# Viết API lấy toàn bộ sản phẩm
@app.get('/products')
def get_products(request:Request):
    return create_response(request, status.HTTP_200_OK, "Lấy danh sách sản phẩm thành công", products)

# Viết API lấy sản phẩm theo id
@app.get('/products/{id}')
def get_product_by_id(request: Request, id: int, number):
    int(number)
    for product in products:
        if product['id'] == id:
            return create_response(request, status.HTTP_200_OK, "Lấy sản phẩm theo id thành công", product)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Sản phẩm không tồn tại"
    )
    
@app.exception_handler(HTTPException)
def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    response = create_response(request, exc.status_code, "Failed", None, exc.detail)
    return JSONResponse(
        status_code = exc.status_code,
        content = response.model_dump()
    )

@app.exception_handler(Exception)
def global_exception_handler(
    request: Request,
    exc: Exception
):
    response = create_response(request, status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal server error", None, str(exc))
    return JSONResponse(
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
        content = response.model_dump()
    )
