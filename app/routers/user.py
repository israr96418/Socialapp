from fastapi import APIRouter, status, Depends,HTTPException
from sqlalchemy.orm import Session

from .. import database, schema, utils, models,oauth

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.get("/{id}",response_model=schema.outschema)
def get_single_user(id: int, db: Session = Depends(database.get_db),
                    get_current_user: int = Depends(oauth.get_current_user)):
    data = db.query(models.User).filter(models.User.id == id).first()

    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not found")

    return data
