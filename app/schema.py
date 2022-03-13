from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.types import conint


class singup(BaseModel):
    id: int
    name: str
    password: str
    email: str
    is_active: Optional[str] = True


    class Config:
        orm_mode = True


class outschema(BaseModel):
    id: int
    name: str
    email: str
    is_active: Optional[str] = True

    class Config:
        orm_mode = True


class Post(BaseModel):
    id: int
    name: str
    description: str
    address: str

    class Config:
        orm_mode = True


class user(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class outschema_for_all_post(BaseModel):
    id: int
    name: str
    description: str
    address: str
    created_at: datetime
    owner_id: int
    owner: user

    class Config:
        orm_mode = True


class post_vote(BaseModel):
    Post: outschema_for_all_post
    vote: int

    class Config:
        orm_mode = True


class out_schema_for_user(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class login(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class Token_data(BaseModel):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class vote(BaseModel):
    post_id: int
    dir: conint(le=1)


class out_schema_for_create_post(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class updatePost(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class outschema_for_updatedPost(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class for_password_changing(BaseModel):
    old_password: str
    new_password: str

    class Config:
        orm_mode = True


class PasswordChangeInSchema(BaseModel):
    old_password: str
    new_password: str

    class Config:
        orm_mode = True


class outschema_password_changing(BaseModel):
    password: str

    class Config:
        orm_mode = True


class ForgetPassword(BaseModel):
    email: str
    new_password: str

    class Config:
        orm_mode = True

