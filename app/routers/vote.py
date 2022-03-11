from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app import database, schema, oauth, models

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote_for_post(vote: schema.vote, db: Session = Depends(database.get_db),
                  get_current_user: int = Depends(oauth.get_current_user)):
    id_of_post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not id_of_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Your Post with id {id_of_post} is not found")

    vote_query = db.query(models.vote).filter(models.vote.post_id == vote.post_id,
                                              models.vote.user_id == get_current_user.id)

    found_vote = vote_query.first()

    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"User{get_current_user.id} has been already like post with id {vote.post_id}")
        new_vote = models.vote(post_id = vote.post_id, user_id = get_current_user.id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)

        return {"message": "Your vote has been successfully addes"}

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Your post with id {vote.post_id} does,t exist")

        vote_query.delete(synchronize_session = False)
        db.commit()

        return {"message":"Your post has been successfuly unlilked"}



