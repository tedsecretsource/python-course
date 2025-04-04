import logging
from fastapi import APIRouter, Depends
from typing import List, Annotated
from sqlmodel import Session, select

from ..models.Users import User
from ..database_connection import get_db_session

router = APIRouter(
    tags=["Users"],
    prefix="/users",
)

@router.get("/", response_model=List[User], include_in_schema=True)
async def read_users(session: Annotated[Session, Depends(get_db_session)]):
    logging.debug("Fetching users from the database.")
    statement = select(User)  # Select all users from the User table
    users = session.exec(statement).all()  # Execute the query and fetch all users
    logging.info(f"Fetched {len(users)} users from the database.")
    return users