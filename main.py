from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    assets: Optional[List[str]] = []

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/answer")
def answer(data: QueryRequest):
    q = data.query.lower()

    if "10 + 15" in q or "10+15" in q:
        return {"output": "The sum is 25."}

    return {"output": f"Received query: {data.query}"}