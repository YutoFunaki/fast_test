from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from db import session
from model import UserTable, User

app = FastAPI()

#　ユーザー情報一覧取得
@app.get("/get_user_list")
def get_user_list():
    users = session.query(UserTable).all()
    return jsonable_encoder(users)

# ユーザー情報取得(id指定)
@app.get("/get_user/{user_id}")
def get_user(user_id: int):
    user = session.query(UserTable).\
        filter(UserTable.id == user_id).first()
    return user


# ユーザ情報登録
@app.post("/post_user")
def post_user(user: User):
    db_user = UserTable(name=user.name, email=user.email, password=user.password)
    session.add(db_user)
    session.commit()
    return jsonable_encoder(db_user)

# ユーザ情報更新
@app.put("/change_users/{user_id}")
def put_users(user: User, user_id: int):
    target_user = session.query(UserTable).\
        filter(UserTable.id == user_id).first()
    target_user.name = user.name
    target_user.email = user.email
    session.commit()

