from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from pydantic import EmailStr

from app.CRUD import user_crud
from app.Database import db
from app.Models import schemas
router = APIRouter(
    prefix="/user",
    tags=["User"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseUser)
async def create_user(user: schemas.BaseUser, db: Session = Depends(db.get_db)):
    db_user = user_crud.get_user_by_username_or_email(user, db)

    if db_user.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email or username taken")
    user_crud.create_user(user, db)
    return db_user.first()

@router.get("/{username}", status_code=status.HTTP_200_OK, response_model=schemas.ResponseUser)
async def get_user_by_notes(username: str, db: Session = Depends(db.get_db)):
    db_user = user_crud.get_user_by_username(username=username, db=db).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    return db_user
    
@router.delete("/{email}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_by_email(email: EmailStr, db: Session = Depends(db.get_db)):
    db_user = user_crud.get_user_by_email(email=email, db=db)
    if db_user.first() is None: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    db_user.delete(synchronize_session=False)
    db.commit()