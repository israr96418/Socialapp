from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import database, schema, utils, models

router = APIRouter(
    prefix="/forgot",
    tags=["forgot_password"]
)


@router.post("/")
def forgot_password(user: schema.ForgetPassword, db: Session = Depends(database.get_db)):
    if utils.pythonRegEx_for_email(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Enter valid email_address")

    data = db.query(models.User).filter(models.User.email == user.email).first()
    if data:
        password_validation = utils.password_validation(user.new_password)
        hashPassword= utils.hashing_password(password_validation)
        data.password = hashPassword
        db.commit()
        return {"message": "password has been successfully change"}
    else:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"your email '{user.email}' are register")
