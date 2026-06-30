from fastapi import FastAPI
from pydantic import BaseModel, Field

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000},
    {"id": 3, "name": "Screen", "price": 400000}
]

class CreateProduct(BaseModel):
    id:int
    name:str
    price:float = Field(gt=0)

class UpdateProduct(BaseModel):
    name: str 
    price: float

app = FastAPI()

@app.get("/")
def get_root():
    return {
        "message": "Xin chào, chào mừng đến với server của tôi"
    }
    
@app.get("/products")
def get_products():
    return {
        "data": products,
        "message": "Lấy danh sách tất cả sản phẩm"
    }
    
# Lấy sản phẩm theo id
@app.get('/product/{product_id}')
def get_product_by_id(product_id):
    for product in products:
        if product_id == str(product['id']):    
            return {
                "data": product
            }
    return {
        "data": None,
        "message": "Không tìm thấy sản phẩm"
    }
    
# Lấy sản phẩm theo khoảng giá
@app.get('/product')
def get_product_by_price(start_price: float, end_price: float):
    filter_products = []
    for p in products:
        if start_price <= p['price'] <= end_price:
            filter_products.append(p)
    if filter_products:
        return {
            "message": "Danh sách sản phẩm tìm được",
            "data": filter_products
        }
    return {
        "message": "Không có sản phẩm nào trong khoảng giá",
        "data": None
    }
    
@app.post('/product')
def create_product(new_product: CreateProduct):
    products.append({
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price
    })
    return {
        "message": "Thêm mới sản phẩm thành công",
        "data": new_product
    }
    
@app.put('/product/{product_id}')
def update_product(product_id: int, update_product: UpdateProduct):
    for p in products:
        if p['id'] == product_id:
            p['name'] = update_product.name
            p['price'] = update_product.price
            return {
                "message": "Cập nhật thông tin sản phẩm thành công",
                "data": {
                    "id": product_id,
                    "name": update_product.name,
                    "price": update_product.price
                }
            }
    return {
        "message": "Không tìm thấy sản phẩm",
        "data": None
    }

@app.delete('/product/{product_id}')
def delete_product(product_id: int):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return {
                "message": "Xóa sản phẩm thành công",
                "data": product
            }
    return {
        "message": "Không tìm thấy sản phẩm cần xóa",
        "data": None
    }