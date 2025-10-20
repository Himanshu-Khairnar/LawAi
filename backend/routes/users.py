from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/")
def get_users():
    return {"users": ["test_user"]}
