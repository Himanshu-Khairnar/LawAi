from fastapi import FastAPI
from routes import usersRoutes
from routes import notebookRoutes
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from models import user
from routes import chatRoutes

Base.metadata.create_all(bind=engine)
app = FastAPI(title="LawAI Backend")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(usersRoutes.router)
app.include_router(chatRoutes.router)
app.include_router(notebookRoutes.router)


@app.get("/")
def root():
    return {"message": "LawAI backend running!"}
