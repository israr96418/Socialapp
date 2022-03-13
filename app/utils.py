import re

from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from . import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashing_password(password):
    print("password at hash", password)
    return pwd_context.hash(password)


def password_verification(plan_passwrd, hash_passwrd):
    passwrd_matching = pwd_context.verify(plan_passwrd, hash_passwrd)
    return passwrd_matching


def password_validation(password):
    if not re.findall(r'.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z])(?=.*[@#$%^&+=]).*$', password):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"Password must contain at least 8 character ,at least 1 alphabet, number and special charater")
    else:
        return password


def pythonRegEx_for_email(email):
    if not re.findall(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', email):
        return True
    else:
        return False


def email_verification(id, email, name, db: Session):
    if pythonRegEx_for_email(email):
        raise HTTPException(status_code=409, detail='Please enter valid email-address')

    id = db.query(models.User).filter(models.User.id == id).first()
    if id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Your id must be unique")

    register_email = db.query(models.User).filter(models.User.email == email).first()
    register_user = db.query(models.User).filter(models.User.name == name).first()

    if register_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"An Account already register with your email")
    if register_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"An Account already register with your username")


def password_changing(plan_passwrd, hash_passwrd):
    passwrd_matching = pwd_context.verify(plan_passwrd, hash_passwrd)
    if passwrd_matching:
        return True
    else:
        return False
