from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, models, utils, oauth

router = APIRouter(
    prefix="/login",
    tags=["login"]
)


@router.post("/", status_code=status.HTTP_200_OK)
def login(login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == login.username).first()
    print("user", user)

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials(email)")

    if not utils.password_verification(login.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials(password)")

    access_token = oauth.create_acces_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer_token"}



