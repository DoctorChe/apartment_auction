from typing import Optional

from sqlalchemy.orm import Session

from backend import models, schemas


def get_or_create_user(db: Session, name: str) -> schemas.User:
    if user := read_user_by_name(db, name):
        return user
    else:
        return create_user(db, name=name)


def read_user_by_name(db: Session, name: str) -> Optional[schemas.User]:
    return db.query(models.User).filter(models.User.name == name).first()


def create_user(db: Session, name: str) -> schemas.User:
    user = models.User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
