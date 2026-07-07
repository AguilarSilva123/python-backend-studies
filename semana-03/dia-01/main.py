from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
         "message":"Hello, Backend! Welcome to my API"
    } 

@app.get("/about")
def about():
    return {
        "name": "João",
        "profession": "Backend Developer Student"
    }   

@app.get("/status")
def status():
    return {
        "status": "online"
    } 