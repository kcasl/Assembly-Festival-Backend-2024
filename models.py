from sqlalchemy import Column, String, Float, VARCHAR, Double, Integer
from database import Base

class User(Base):
    __tablename__ = 'users'

    std_id = Column(VARCHAR(100), unique=True, primary_key=True, nullable=False)
    username = Column(VARCHAR(100), unique=True, primary_key=True, nullable=False)
    password = Column(VARCHAR(100), primary_key=True, nullable=False)
    capital = Column(Double, default=0.00)

class User_Stock(Base):
    __tablename__ = 'users_stock'

    std_id = Column(VARCHAR(100), unique=True, primary_key=True, nullable=False)
    stock1 = Column(Integer, nullable=False)
    stock2 = Column(Integer, nullable=False)
    stock3 = Column(Integer, nullable=False)
    stock4 = Column(Integer, nullable=False)

