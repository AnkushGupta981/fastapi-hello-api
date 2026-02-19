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
