from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
    }

@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: int, post_id: int):
    return {
        "user": user_id,
        "post": post_id,
    }

@app.get("/search")
def search(name: str):
    return {
        "search": name,
    }

@app.get("/products")
def products(category: str, min_price: float):
    return {
        "category": category,
        "min_price": min_price,
    }

@app.get("/clients")
def clients(city: str | None= None):
    return {
        "city": city,
    }
