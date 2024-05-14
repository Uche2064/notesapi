from app.Models import models, schemas
from app.Utilities import utils
from datetime import datetime

from sqlalchemy.orm import Session


def get_all_notes(skip: int, limit: int, db: Session):
    return db.query(models.Note).offset(skip).limit(limit).all()


def create_note(note: schemas.BaseNotes,  db: Session):
    new_note = models.Note(**note.model_dump())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


def delete_note(id: int, db: Session):
    note = db.query(models.Note).filter(models.Note.id == id).first()
    db.delete(note)
    db.commit()
    return note

def update_note(id: int, updated_note: schemas.UpdateNote, db: Session):
    db_note = db.query(models.Note).filter(models.Note.id == id)
    if db_note.first() is None: 
        return None
    new_note = {
        "title": updated_note.title,
        "content": updated_note.content,
        "updated_at": datetime.now()
    }
    db_note.update(new_note) 
    db.commit()
    return db_note.first()