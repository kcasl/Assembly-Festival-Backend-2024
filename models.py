from sqlalchemy import Column, String, Float, VARCHAR, Double
from database import Base

class User(Base):
    __tablename__ = 'users'

    std_id = Column(VARCHAR(100), unique=True, primary_key=True, nullable=False)
    username = Column(VARCHAR(100), unique=True, primary_key=True, nullable=False)
    password = Column(VARCHAR(100), primary_key=True, nullable=False)
    capital = Column(Double, default=0.00)
