from fastapi import APIRouter
from sqlalchemy.orm import Session
from models.chat import Chat
from database import SessionDep
import requests

RAG_API_URL = "http://127.0.0.1:5001/ask"

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def save_chat(chat: Chat, db: SessionDep):
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


@router.post("/ask")
def ask_question(chat: Chat, db: SessionDep):
    question = chat.question
    user_id = chat.user_id

    response = requests.post(RAG_API_URL, json={"query": question})
    answer = response.json().get("response", "No answer found")

    chat.answer = answer
    db.add(chat)
    db.commit()
    db.refresh(chat)

    return {"user_id": user_id, "question": question, "answer": answer}
