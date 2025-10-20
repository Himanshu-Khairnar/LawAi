from fastapi import FastAPI
from routes import users
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from models import user

Base.metadata.create_all(bind=engine)
app = FastAPI(title="LawAI Backend")

origins = [
    "http://localhost:3000",  # your Next.js dev server
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allowed frontend URLs
    allow_credentials=True,
    allow_methods=["*"],             # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],             # Allow all headers
)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "LawAI backend running!"}
