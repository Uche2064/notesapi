from pydantic import EmailStr
from app.Models import schemas
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.Models import models
from app.Utilities import utils

def get_user_by_email(email: EmailStr, db: Session):
    return db.query(models.User).filter(models.User.email == email)  
    
    
def get_user_by_username(username: str, db: Session):
    return db.query(models.User).filter(models.User.username == username)  

def get_user_by_username_or_email(user, db: Session):
    return db.query(models.User).filter(or_(models.User.username == user.username, models.User.email == user.email))

def create_user(user: schemas.BaseUser,  db: Session):
    user.password = utils.hash_pwd(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user