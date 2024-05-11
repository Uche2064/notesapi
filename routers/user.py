from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app import schemas, db, models
from sqlalchemy import or_
router = APIRouter(
    prefix="/user",
    tags=["User"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseUser)
async def create_user(user: schemas.BaseUser, db: Session = Depends(db.get_db)):
    db_user = await db.query(models.User).filter(or_(models.User.username == user.username, models.User.email == user.email))
    
    if db_user.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email or username taken")
    
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return db_user.first()

@router.get("/{username}", status_code=status.HTTP_200_OK)
async def get_user_with_notes(username: str, db: Session = Depends(db.get_db)):
    db_user = db.query(models.User).filter(models.User.username == username).first()  
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    
    return db_user
    