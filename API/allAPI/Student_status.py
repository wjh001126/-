from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from API.database import get_db, Base
from sqlalchemy import Column, Integer, String

app03 = APIRouter()

