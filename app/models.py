from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=True)
    description = Column(String(30), nullable=True)
    address = Column(String(30), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("user.id", ondelete='CASCADE'), nullable=False)

    # return class of another model(sqlalchemy model)
    owner = relationship("User")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=True)
    password = Column(String(3000), nullable=False)
    email = Column(String(30), nullable=False)
    is_active = Column(Boolean, nullable=True)


class vote(Base):
    __tablename__ = "vote"
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id", ondelete='CASCADE'), primary_key=True, nullable=False)
