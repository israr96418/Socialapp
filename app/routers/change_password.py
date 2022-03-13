from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session

from .. import database, oauth, models,schema,utils

router = APIRouter(
    prefix="/change_password",
    tags=["Change_password"]
)


@router.post("/")
def change_password(user :schema.PasswordChangeInSchema,db: Session = Depends(database.get_db),
                    get_current_user:models.User= Depends(oauth.get_current_user)):
    if not utils.password_changing(user.old_password, get_current_user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"old_password is wrong")
    else:
        password_validation = utils.password_validation(user.new_password)
        get_current_user.password = utils.hashing_password(password_validation)
        db.commit()
        return {"message":"your password has been successfully change"}
