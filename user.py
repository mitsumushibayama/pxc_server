from pydantic import BaseModel

class User(BaseModel):
    name: str
    height: int
    gender: str
    user_picture_URL: str

