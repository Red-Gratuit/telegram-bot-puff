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
        {
            "id": 16,
            "name": "16K JNR",
            "price": 25,
            "puffs": "16000 bouffées",
            "nicotine": "2%",
            "battery": "Rechargeable USB-C",
            "image": "https://via.placeholder.com/400x300?text=16K+JNR"
        },
        {
            "id": 18,
            "name": "18K JNR",
            "price": 30,
            "puffs": "18000 bouffées",
            "nicotine": "2%",
            "battery": "Rechargeable USB-C",
            "image": "https://via.placeholder.com/400x300?text=18K+JNR"
        }
    ]

