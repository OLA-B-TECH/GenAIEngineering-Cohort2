# calculator.py
# A simple calculator with add and subtract functions
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/add")
def add(a, b):
    """Add two numbers and return the result."""
    result = float(a) + float(b)
<<<<<<< HEAD
    #result = a+b
=======
    # result = a+b
>>>>>>> efc449e (added week3 content)
    return {"operation": "add", "a": a, "b": b, "result": result}

@app.get("/subtract")
def subtract(a, b):
    """Subtract b from a and return the result."""
    result = float(a) - float(b)
<<<<<<< HEAD
    #result = a-b
=======
    # result = a-b
>>>>>>> efc449e (added week3 content)
    return {"operation": "subtract", "a": a, "b": b, "result": result}

@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Calculator API is running. Use /add or /subtract endpoints."}


# Main program
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)


'''
import requests
<<<<<<< HEAD
response = requests.get("http://localhost:8001/add", params={"a": 5, "b": 3})
=======
response = requests.get("http://localhost:9321/add", params={"a": 5, "b": 3})
>>>>>>> efc449e (added week3 content)
print(response.json())
'''
