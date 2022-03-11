from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from .. import database, schema, utils, models

router = APIRouter(
    prefix="/signup",
    tags=["user"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.out_schema_for_user)
def Sign_up(user: schema.singup, db: Session = Depends(database.get_db)):
    hash_password = utils.hasing_password(user.password)
    user.password = hash_password

    data = models.User(**user.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data