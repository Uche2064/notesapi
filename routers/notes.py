from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.Models import schemas
from app.Database import db
from app.CRUD import notes_crud
router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ResponseNote])
def get_notes(skip = 0, limit = 10, db: Session = Depends(db.get_db)):
    return notes_crud.get_all_notes(skip=skip, limit=limit, db=db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseNote)
def create_note(note: schemas.BaseNotes, db: Session = Depends(db.get_db)):
    return notes_crud.create_note(note=note, db=db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note_by_id(id: int, db: Session = Depends(db.get_db)):
    if notes_crud.delete_note(id, db) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ResponseNote)
def update_note_by_id(id: int, updated_note: schemas.UpdateNote, db: Session = Depends(db.get_db)):
    update_note = notes_crud.update_note(id, updated_note, db) 
    if update_note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return update_note