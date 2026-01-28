from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK pour commencer
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/ping")
def ping():
    return {"message": "Backend OK 🔥"}

@app.get("/api/products")
def products():
    return [
        {"id": 1, "name": "Burger", "price": 7.5},
        {"id": 2, "name": "Tacos", "price": 6.0},
        {"id": 3, "name": "Kebab", "price": 6.5},
    ]
