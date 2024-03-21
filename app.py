from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Instance de l'application
app = FastAPI(
    title="Kubernetes Evaluation",
    description="Rendu de NELLY GUEPNANG.",
    version="1.0.0"
)

# Modèle Pydantic pour les données utilisateur
class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None

# Base de données fictive
db: List[User] = []

@app.get("/")
def read_root():
    return {"Message": "Welcome to my Kubernetes deployment"}

@app.post("/users/", response_model=User, status_code=201)
def create_user(user: User):
    db.append(user)
    return user

@app.get("/users/", response_model=List[User])
def read_users():
    return db

@app.get("/users/count", response_model=int)
def count_users():
    return len(db)
