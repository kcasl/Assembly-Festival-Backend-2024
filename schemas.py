from pydantic import BaseModel

class UserCreate(BaseModel):
    std_id: str
    username: str
    password: str
    capital: float

class UserLogin(BaseModel):
    std_id: str
    password: str

class Info(BaseModel):
    std_id: str

class Money(BaseModel):
    std_id: str
    capital: float

class Stock1_SB(BaseModel):
    std_id: str
    token: str
    stock1: int

class Stock2_SB(BaseModel):
    std_id: str
    token: str
    stock2: int

class Stock3_SB(BaseModel):
    std_id: str
    token: str
    stock3: int

class Stock4_SB(BaseModel):
    std_id: str
    token: str
    stock4: int

# class UserUpdate(BaseModel):
#     capital: float = None

# class UserResponse(BaseModel):
#     std_id: str
#     username: str
#     password: str
#     capital: float

    class Config:
        orm_mode = True
