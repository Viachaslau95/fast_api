from fastapi import FastAPI

app = FastAPI(
    title='Trading App'
)

fake_users = [
    {'id': 1, 'name': 'Alex', 'age': 23},
    {'id': 2, 'name': 'Maks', 'age': 20},
    {'id': 3, 'name': 'Den', 'age': 32},
]


@app.get('/users')
def get_users():
    return fake_users


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in fake_users if user['id'] == user_id]


fake_trades = [
    {'id': 1, 'current': 'BTC', 'total': 2},
    {'id': 2, 'current': 'ADA', 'total': 400},
    {'id': 3, 'current': 'ETH', 'total': 14},
]


@app.get('/trades')
def get_trades(limit: int = 2):
    return fake_trades[:limit]


