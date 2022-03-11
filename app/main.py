from fastapi import FastAPI
from . import models,database
from .routers import login,sign_up,post,vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=database.engine)

# only these origin are allowed to request out server
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

# this means request will be accepted from all of the origin
origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sign_up.router)
app.include_router(login.router)
app.include_router(post.router)
app.include_router(vote.router)

@app.get("/")
def data():
    return {"message":"hello World!!"}
