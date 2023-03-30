from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    name: str
    age: int


@app.post("/my_api_endpoint")
async def my_api_endpoint(input_data: InputData):
    output_data = {"message": f"Hello, {input_data.name}! You are {input_data.age} years old."}
    return output_data
