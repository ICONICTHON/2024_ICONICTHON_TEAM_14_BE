from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..utils import log_info

router = APIRouter()

class LoginRequest(BaseModel):
    username: str

active_users = set()

@router.post("/login")
async def login(request: LoginRequest):
    username = request.username.strip()
    if not username:
        raise HTTPException(status_code=400, detail="Username cannot be empty")
    active_users.add(username)
    log_info(f"User '{username}' logged in")
    return {"message": f"Welcome, {username}!"}
