from sqlalchemy.orm import Session
import models
import schemas

from stock_price_management import *

# 새로운 사용자 생성
def create_user(db: Session, user: schemas.UserCreate):

    db_user = models.User(std_id=user.std_id, username=user.username, password=user.password, capital=user.capital)
    db_stock = models.User_Stock(std_id=user.std_id,stock1=0, stock2=0, stock3=0, stock4=0)

    db.add(db_user)
    db.add(db_stock)

    db.commit()

    db.refresh(db_user)
    db.refresh(db_stock)

    return db_user

# 사용자 정보 업데이트
def update_user(db: Session, std_id: str):
    db_user = db.query(models.User).filter(models.User.std_id == std_id).first()
    db_stock = db.query(models.User_Stock).filter(models.User_Stock.std_id == std_id).first()
    if db_user and db_stock:
        db_user.capital = (
            db_user.capital + #기본 자금
            db_stock.stock1 * stock1_price_list[-1] + # 주식 1 가격 합
            db_stock.stock2 * stock2_price_list[-1] + # 주식 2 가격 합
            db_stock.stock3 * stock3_price_list[-1] + # 주식 3 가격 합
            db_stock.stock4 * stock4_price_list[-1]   # 주식 4 가격 합
        )
        db.commit()
        db.refresh(db_user)
        db.refresh(db_stock)
    return db_user

# 사용자 조회
def get_user(db: Session, std_id: str):
    return db.query(models.User).filter(models.User.std_id == std_id).first()

def save_token(db: Session, std_id: str, token: str):
    db_user = db.query(models.User).filter(models.User.std_id == std_id).first()
    db_user.token = token
    db.commit()
    db.refresh(db_user)
    return db_user


def buy_stock1c(db: Session, user: schemas.Stock1_SB):
    db_user = db.query(models.User).filter(models.User.std_id == user.std_id).first()
    db_stock = db.query(models.User_Stock).filter(models.User_Stock.std_id == user.std_id).first()
    if (db_user and db_stock) and (user.token == db_user.token):
        update_capital = db_user.capital - (stock1_price_list[-1] * user.stock1)
        if update_capital < 0:
            return "매수를 위한 자금이 부족합니다. 게임머니를 충전해주세요."
        else:
            db_user.capital = update_capital
            db_stock.stock1 = user.stock1

            db.commit()

            db.refresh(db_user)
            db.refresh(db_stock)
            return db_stock
    else:
        return "잘못된 접근입니다. 관리자에게 문의해주세요."
def sell_stock1c(db: Session, user: schemas.Stock1_SB):
    db_user = db.query(models.User).filter(models.User.std_id == user.std_id).first()
    db_stock = db.query(models.User_Stock).filter(models.User_Stock.std_id == user.std_id).first()

    if (db_user and db_stock) and (user.token == db_user.token):
        update_capital = db_user.capital + (stock1_price_list[-1] * user.stock1)

        if db_stock.stock1 - user.stock1 < 0:
            return "주식의 보유량이 매도량보다 적습니다. 다시 시도해주세요."
        else:
            db_user.capital = update_capital
            db_stock.stock1 -= user.stock1

        db.commit()

        db.refresh(db_user)
        db.refresh(db_stock)
        return db_stock
    else:
        return "잘못된 접근입니다. 관리자에게 문의해주세요."

def buy_stock2c(db: Session, user: schemas.Stock2_SB):
    db_user = db.query(models.User).filter(models.User.std_id == user.std_id).first()
    db_stock = db.query(models.User_Stock).filter(models.User_Stock.std_id == user.std_id).first()
    if (db_user and db_stock) and (user.token == db_user.token):
        update_capital = db_user.capital - (stock2_price_list[-1] * user.stock2)
        if update_capital < 0:
            return "매수를 위한 자금이 부족합니다. 게임머니를 충전해주세요."
        else:
            db_user.capital = update_capital
            db_stock.stock2 = user.stock2

            db.commit()

            db.refresh(db_user)
            db.refresh(db_stock)
            return db_stock
    else:
        return "잘못된 접근입니다. 관리자에게 문의해주세요."
def sell_stock2c(db: Session, user: schemas.Stock2_SB):
    db_user = db.query(models.User).filter(models.User.std_id == user.std_id).first()
    db_stock = db.query(models.User_Stock).filter(models.User_Stock.std_id == user.std_id).first()

    if (db_user and db_stock) and (user.token == db_user.token):
        update_capital = db_user.capital + (stock2_price_list[-1] * user.stock2)

        if db_stock.stock2 - user.stock2 < 0:
            return "주식의 보유량이 매도량보다 적습니다. 다시 시도해주세요."
        else:
            db_user.capital = update_capital
            db_stock.stock2 -= user.stock2

        db.commit()

        db.refresh(db_user)
        db.refresh(db_stock)
        return db_stock
    else:
        return "잘못된 접근입니다. 관리자에게 문의해주세요."

def buy_stock3c(db: Session, user: schemas.Stock3_SB):
    db_user = db.query(models.User).filter(models.User.std_id == user.std_id).first()
    db_stock = db.query(models.User_Stock).filter(models.User_Stock.std_id == user.std_id).first()
    if (db_user and db_stock) and (user.token == db_user.token):
        update_capital = db_user.capital - (stock3_price_list[-1] * user.stock3)
        if update_capital < 0:
            return "매수를 위한 자금이 부족합니다. 게임머니를 충전해주세요."
        else:
            db_user.capital = update_capital
            db_stock.stock3 = user.stock3

            db.commit()

            db.refresh(db_user)
            db.refresh(db_stock)
            return db_stock
    else:
        return "잘못된 접근입니다. 관리자에게 문의해주세요."
def sell_stock3c(db: Session, user: schemas.Stock3_SB):
    db_user = db.query(models.User).filter(models.User.std_id == user.std_id).first()
    db_stock = db.query(models.User_Stock).filter(models.User_Stock.std_id == user.std_id).first()

    if (db_user and db_stock) and (user.token == db_user.token):
        update_capital = db_user.capital + (stock3_price_list[-1] * user.stock3)

        if db_stock.stock3 - user.stock3 < 0:
            return "주식의 보유량이 매도량보다 적습니다. 다시 시도해주세요."
        else:
            db_user.capital = update_capital
            db_stock.stock3 -= user.stock3

        db.commit()

        db.refresh(db_user)
        db.refresh(db_stock)
        return db_stock
    else:
        return "잘못된 접근입니다. 관리자에게 문의해주세요."

def buy_stock4c(db: Session, user: schemas.Stock4_SB):
    db_user = db.query(models.User).filter(models.User.std_id == user.std_id).first()
    db_stock = db.query(models.User_Stock).filter(models.User_Stock.std_id == user.std_id).first()
    if (db_user and db_stock) and (user.token == db_user.token):
        update_capital = db_user.capital - (stock4_price_list[-1] * user.stock4)
        if update_capital < 0:
            return "매수를 위한 자금이 부족합니다. 게임머니를 충전해주세요."
        else:
            db_user.capital = update_capital
            db_stock.stock4 = user.stock4

            db.commit()

            db.refresh(db_user)
            db.refresh(db_stock)
            return db_stock
    else:
        return "잘못된 접근입니다. 관리자에게 문의해주세요."
def sell_stock4c(db: Session, user: schemas.Stock4_SB):
    db_user = db.query(models.User).filter(models.User.std_id == user.std_id).first()
    db_stock = db.query(models.User_Stock).filter(models.User_Stock.std_id == user.std_id).first()

    if (db_user and db_stock) and (user.token == db_user.token):
        update_capital = db_user.capital + (stock4_price_list[-1] * user.stock4)

        if db_stock.stock4 - user.stock4 < 0:
            return "주식의 보유량이 매도량보다 적습니다. 다시 시도해주세요."
        else:
            db_user.capital = update_capital
            db_stock.stock4 -= user.stock4

        db.commit()

        db.refresh(db_user)
        db.refresh(db_stock)
        return db_stock
    else:
        return "잘못된 접근입니다. 관리자에게 문의해주세요."