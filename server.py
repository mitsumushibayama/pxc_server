from fastapi import FastAPI
import uvicorn
import userdb
import user


app = FastAPI()

@app.get("/users")
def get_user():
    return db.get_user()

@app.post("/users")
def post_user(user: user.User):
    return db.post_user()

@app.get("/users/{user_id}")
def get_id_user(user_id: int):
    return db.get_id_user(user_id)

@app.post("/users/{user_id}")
def update_user(user_id: int, user: user.User):
    return userdb.update_user(user_id,user)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 80)


