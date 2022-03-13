from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from .. import database, schema, utils, models

router = APIRouter(
    prefix="/signup",
    tags=["SignUp"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.out_schema_for_user)
def sign_up(user: schema.singup, db: Session = Depends(database.get_db)):
    # first check password with out python reqular expression
    password_validation=utils.password_validation(user.password)
    email = utils.email_verification(user.id,user.email,user.name,db)
    print("Email", email)

    hash_password = utils.hashing_password(password_validation)
    user.password = hash_password

    data = models.User(**user.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data