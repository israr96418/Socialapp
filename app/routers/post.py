from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException,Response
from sqlalchemy import func
from sqlalchemy.orm import Session

from .. import database, schema, oauth, models

router = APIRouter(
    prefix="/post",
    tags=["Post"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.out_schema_for_create_post)
def Post_Create(post: schema.Post, db: Session = Depends(database.get_db),
                get_current_user: int = Depends(oauth.get_current_user)):
    print("Name of the current user that we logged in: ", get_current_user.id)
    data = models.Post(owner_id=get_current_user.id, **post.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data


# to get all post
@router.get("/", response_model=List[schema.post_vote])
# @router.get("/")
def get_all_post(get_curretn_user: int = Depends(oauth.get_current_user), db: Session = Depends(database.get_db)
                 , limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # this query return only those post which is created by that owner that we logged in
    # get_post = db.query(models.Post).filter(models.Post.owner_id== get_curretn_user.id).all()

    # result = db.query(models.Post).all()
    result = db.query(models.Post, func.count(models.vote.post_id).label("vote")).join(models.vote,
                                                                                       models.vote.post_id == models.Post.id,
                                                                                       isouter=True).group_by(
        models.Post.id).limit(limit).offset(skip).all()

    print("ajsdhfasjdf", result)

    return result


@router.get("/{id}", response_model=schema.post_vote)
def get_single_post(id: int, db: Session = Depends(database.get_db),
                    get_current_user: int = Depends(oauth.get_current_user)):
    data = db.query(models.Post, func.count(models.vote.post_id).label("vote")).join(models.vote,
                                                                                     models.vote.post_id == models.Post.id,
                                                                                     isouter=True).group_by(
        models.Post.id).filter(models.Post.id == id).first()

    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Your post with id {id} is not found")
    return data


@router.put("/{id}", response_model=schema.outschema_for_updatedPost)
def update_post(id: int,update:schema.updatePost, db: Session = Depends(database.get_db),
                get_current_user: int = Depends(oauth.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Your post with id {id} is not found")

    if post.owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized ")

    post_query.update(update.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def update_post(id: int, db: Session = Depends(database.get_db),
                get_current_user: int = Depends(oauth.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Your post with id {id} is not found")

    if post.owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized ")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
