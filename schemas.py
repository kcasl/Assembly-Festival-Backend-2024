from pydantic import BaseModel

class UserCreate(BaseModel):
    std_id: str
    username: str
    password: str
    capital: float

class UserLogin(BaseModel):
    std_id: str
    password: str

class UserUpdate(BaseModel):
    capital: float = None

# class UserResponse(BaseModel):
#     std_id: str
#     username: str
#     password: str
#     capital: float

    class Config:
        orm_mode = True
