#  FOR PRACTICE PURPOSE


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hi i am learning the fast api framework"}

@app.get("/about")
def about():
    return {"message":" This is the about page of the Fastapi application."}

@app.get("/aboutme")
def about_me():
    databoj = {
        "name": "AFAQ KHAN",
        "age": 23,
        "profession": "Software Developer",
        "hobbies": ["coding", "reading", "traveling"]
    }
    return databoj


@app.get("/contact")
def contact():
    return {"email": "support@example.com"}


class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginData):
    return {"msg": f"User {data.username} logged in successfully"}




# Pydantic model
class Product(BaseModel):
    id: int
    name: str
    price: float

products = []

# POST route with request body
@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product

# Path parameter route
@app.get("/items/{item_id}")
def read_me(item_id: int):
    return {"product_id": item_id}

# Query parameter route
@app.get("/items/")
def read_item(q: int = 0):
    return {"product is": q}

# Combined path and query parameters
@app.get("/users/{user_id}/items/")
def get_user_items(user_id: int, q: str = None):
    return {"user_id": user_id, "query": q}
    
