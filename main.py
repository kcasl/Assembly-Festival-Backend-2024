from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import random as r
import json
import secrets
import crud
import schemas
import models
from database import engine, get_db
from stock_price_management import *

# 모델 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 사용자 생성
@app.post("/register",
          tags=["계정 관리"],
          summary="고유학번, 비밀번호로 계정 생성 - 프롬프트에서 따로 처리할 예정.")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = crud.create_user(db, user)
        return db_user

    except Exception as e:
        return f"이미 존재하는 계정입니다. 관리자에게 문의해주세요. err : {e}"

# 사용자 정보 조회
@app.post("/login",
          tags=["계정 관리"],
          summary="등록한 정보를 기반으로 로그인. -> DB에서의 쿼리값과 같다면 true 반환.")
def read_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    try:
        db_user = crud.get_user(db, user.std_id)

        if user.password == db_user.password:
            token = secrets.token_urlsafe(16)
            return crud.save_token(db, user.std_id, token)
        else:
            return "비밀번호가 틀립니다. 다시 시도해주세요."
    except Exception as e:
        return f"계정 정보가 존재하지 않습니다. 회원가입 후 이용해주세요. err : {e}"

# 사용자 정보 업데이트
@app.put("/update_capital/{std_id}",
         tags=["계정 관리"],
         summary="자본 정보 업데이트. -> 주식 수 * 해당 주식 가격")
def update_user(std_id: str, db: Session = Depends(get_db)):
    try:
        db_user = crud.update_user(db, std_id)
        return db_user
    except Exception as e:
        return f"계정 정보가 존재하지 않습니다. 관리자에게 문의해주세요. err : {e}"

@app.get("/stock_init",
         tags=["주가 변동 관리"],
         summary="매 라운드 시작할 때 호출할 것. 주식 정보 초기화.")
def stock_init():
    stock_price_init(r.randint(500,700), r.randint(50,70), r.randint(100,200), r.randint(800, 1100))
    root_update()
    return "초기화 및 그래프 시작 성공."

@app.post("/buy_stock1", tags=["매도 / 매수"])
def buy_stock1(user: schemas.Stock1_SB, db: Session = Depends(get_db)):
    return crud.buy_stock1c(db, user)

@app.post("/sell_stock1", tags=["매도 / 매수"])
def sell_stock1(user: schemas.Stock1_SB, db: Session = Depends(get_db)):
    return crud.sell_stock1c(db, user)

@app.post("/buy_stock2", tags=["매도 / 매수"])
def buy_stock1(user: schemas.Stock2_SB, db: Session = Depends(get_db)):
    return crud.buy_stock2c(db, user)

@app.post("/sell_stock2", tags=["매도 / 매수"])
def sell_stock1(user: schemas.Stock2_SB, db: Session = Depends(get_db)):
    return crud.sell_stock2c(db, user)

@app.post("/buy_stock3", tags=["매도 / 매수"])
def buy_stock1(user: schemas.Stock3_SB, db: Session = Depends(get_db)):
    return crud.buy_stock3c(db, user)

@app.post("/sell_stock3", tags=["매도 / 매수"])
def sell_stock1(user: schemas.Stock3_SB, db: Session = Depends(get_db)):
    return crud.sell_stock3c(db, user)

@app.post("/buy_stock4", tags=["매도 / 매수"])
def buy_stock1(user: schemas.Stock4_SB, db: Session = Depends(get_db)):
    return crud.buy_stock4c(db, user)

@app.post("/sell_stock4", tags=["매도 / 매수"])
def sell_stock1(user: schemas.Stock4_SB, db: Session = Depends(get_db)):
    return crud.sell_stock4c(db, user)

@app.get("/stock1", tags=["주가 변동 관리"])
def stock_price1():
    return stock1_return

@app.get("/stock2", tags=["주가 변동 관리"])
def stock_price2():
    return stock2_return

@app.get("/stock3", tags=["주가 변동 관리"])
def stock_price3():
    return stock3_return

@app.get("/stock4", tags=["주가 변동 관리"])
def stock_price4():
    return stock4_return
