from sqlalchemy.orm import Session
import models
import schemas

# 새로운 사용자 생성
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(std_id=user.std_id, username=user.username, password=user.password, capital=user.capital)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# 사용자 정보 업데이트
def update_user(db: Session, std_id: str, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.std_id == std_id).first()
    if db_user:
        if user_update.capital:
            db_user.capital = user_update.capital
        db.commit()
        db.refresh(db_user)
    return db_user

# 사용자 조회
def get_user(db: Session, std_id: str):
    return db.query(models.User).filter(models.User.std_id == std_id).first()
