<<<<<<< HEAD
from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message": "API is working"}

# Sum endpoint
@app.get("/sum")
def calculate_sum(a: int, b: int):
    result = a + b
    return {
        "a": a,
        "b": b,
        "result": result
    }
=======
from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
def predict():
    return {"message": "working"}
>>>>>>> 5e3e0ac247f9228f024a5113fcfc99eed5013218
