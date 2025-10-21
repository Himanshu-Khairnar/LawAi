from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from database import SessionDep
from models.notebook import Notebook
from utils.summarizer import summarize_text
from utils.flashcard_gen import generate_flashcards
from pydantic import BaseModel
import os

router = APIRouter(prefix="/notebook", tags=["NotebookLLM"])


class NotebookCreate(BaseModel):
    user_id: int
    title: str
    description: str | None = None


class SummarizeRequest(BaseModel):
    content: str


class FlashcardRequest(BaseModel):
    content: str


@router.post("/")
def create_notebook(notebook: NotebookCreate, db: SessionDep):
    new_notebook = Notebook(
        user_id=notebook.user_id,
        title=notebook.title,
        description=notebook.description,
    )
    db.add(new_notebook)
    db.commit()
    db.refresh(new_notebook)
    return new_notebook


@router.post("/{notebook_id}/upload")
async def upload_notes(notebook_id: int, file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {"message": "File uploaded successfully!", "file_path": file_path}


@router.post("/{notebook_id}/summarize")
def summarize_notes(request: SummarizeRequest):
    summary = summarize_text(request.content)
    return {"summary": summary}


@router.post("/{notebook_id}/flashcards")
def create_flashcards(request: FlashcardRequest):
    cards = generate_flashcards(request.content)
    return {"flashcards": cards}
