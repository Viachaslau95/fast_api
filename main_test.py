from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int = Field(eq=0)


@app.get("/", response_model=User)
def users():
    return
