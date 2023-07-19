from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title='Trading App'
)

fake_users = [
    {'id': 1, 'name': 'Alex', 'role': "admin"},
    {'id': 2, 'name': 'Maks', 'role': "investor"},
    {'id': 3, 'name': 'Den', 'role': 'trader'},
]


class DegreeType(Enum):
    NEWBIE = 'newbie'
    EXPERT = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType  # nested class


class User(BaseModel):
    id: int
    name: str
    role: str = Field(max_length=15)
    degree: Optional[List[Degree]] = []   # Optional - without "= []" default null


@app.get('/users')
def get_users():
    return fake_users


# response_model = model that we receive from the client for validation
@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user['id'] == user_id]


fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 2.0},
    {'id': 2, 'user_id': 1, 'currency': 'ETH', 'side': 'buy', 'price': 12.0},
    {'id': 3, 'user_id': 1, 'currency': 'ADA', 'side': 'buy', 'price': 120.0},
    {'id': 4, 'user_id': 1, 'currency': 'AVAX', 'side': 'buy', 'price': 30.0},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=7)
    side: str
    price: float = Field(ge=0)


@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}
