from fastapi import FastAPI
from app import models,database
from app.routers import login,sign_up,post,vote,change_password,user,forgotPassword
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=database.engine)
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
app.include_router(change_password.router)
app.include_router(user.router)
app.include_router(forgotPassword.router)


@app.get("/")
def data():
    return {"message":"hello World!!"}
