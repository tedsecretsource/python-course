from fastapi import FastAPI, Request, APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session

from .Users import router as users_router



sample_app = FastAPI(
    title="Sample App API",
    description="This is an example of an application created in FastAPI.",
    version="0.0.1",
    terms_of_service="https://secret-source.eu/",
    contact={
        "name": "Ted Stresen-Reuter",
        "url": "https://secret-source.eu/team/ted",
        "email": "ted@secret-source.eu",
    },
    servers=[
        {
            "url": "http://localhost:8000/api/v1",
            "description": "Production server",
        },
    ],
)
sample_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
sample_app.include_router(APIRouter(), prefix="/api/v1", tags=["Users"])
sample_app.include_router(users_router, prefix="/api/v1", tags=["Users"])

@sample_app.get("/", response_class=HTMLResponse, include_in_schema=False)
def read_root():
    """Root endpoint. Simply announce we are here."""
    return "<head><title>Sample API</title></head>\n<body><h1>Hello, world! Nothing to see here. Move along.</h1></body>"
