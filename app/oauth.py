from datetime import datetime, timedelta

from fastapi import status, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from . config import setting

from . import database, schema, models

# To create jwt we must have the following 3 things
# 1: Algorithms
# 2: Secrete key
# 3: jwt_expiration_time


Oauth_schema = OAuth2PasswordBearer(tokenUrl="login")

ALGORITHMS = setting.algorithms
SECRETE_KEY = setting.secrete_key
JWT_EXPIRATION_TIME = setting.access_token_expiration_time
# print("time ", setting.access_token_expiration_time)

def create_acces_token(data: dict):

    to_encode = data.copy()
    expiration_time = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME)
    print("to_encode", to_encode)
    to_encode.update({"exp": expiration_time})
    print("after updating", to_encode)

    json_web_toke = jwt.encode(to_encode, SECRETE_KEY, algorithm=ALGORITHMS)
    print("json web token: ", json_web_toke)
    return json_web_toke


def verify_access_token(token: str, credential_acception):
    try:
        payload = jwt.decode(token, SECRETE_KEY, algorithms=[ALGORITHMS])
        id: int = payload.get("user_id")
        if id is None:
            raise credential_acception
        token_data = schema.Token_data(id=id)
    except JWTError:
        raise credential_acception

    return token_data


# it will give the current logged in user
# we verify the jwt of the current logged in user
def get_current_user(token: str = Depends(Oauth_schema), db: Session = Depends(database.get_db)):
    credential_acception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Cloud,t Valid Credentials",
                                         headers={"WWW-Authenticate": "bearer"})

    token = verify_access_token(token, credential_acception)
    print("token After returing from verfiy_access_token: ", token.id)
    current_user = db.query(models.User).filter(models.User.id == token.id).first()
    print("user_name: ",current_user.name)

    return current_user
