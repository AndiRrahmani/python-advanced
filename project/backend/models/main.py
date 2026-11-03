import os
import sqlite3

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPExeception
from streamlit import title

from database import create_database, get_connection
from models.authors import AuthorCreate, AuthorsResponse
from models.book import BookCreate,BookResponse

from project.backend.models.authors import AuthorResponse, AuthorCreate
from project.backend.models.book import BookResponse

load_dotenv()
app = FastAPI(title="Simple Book Menagment API")
create_database()


def check_key(x_api_key: str |None = Header(deafult=None)):
    key = os.getenv("API_KEY")
    if key and x_api_key != key:
        raise HTTPExeception(401,"Invalid api key ")


@app.get("/")
def home():
    return {"message":"Book Menagment API", "docs":"/docs"}

@app.get("/authors",response_model=list[AuthorResponse])
def list_authoros():
    with get_connection() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM author ORDER BY id")]

@app.post("/authors", response_models =AuthorResponse, status_code=201, dependencies=[Depends(check_key())])
    try:
        with get_connection() as conn:
            cor =conn.execute("INSERT INTO authors (name) Values(?", (author.name,))
            return {"id":cur.lastrowid, "name":author.name}

    except sqlite3.InternalError:
        raise HTTPExeception(409,"Author already exists")

@app.put("/authors/{author_id}", response_model=AuthorResponse, dependecies=[Depends(check_id())])
def update_author(author_id:int, author:AuthorCreate):
    try:
        with get_connection() as conn:
            cur = conn.execute("UPDATE authors SET name=? WHERE id=?".(author.name, author_id))
            if cur.rowcount ==0:
                raise HTTPExeception(404,"Author not found")
            return  {"id":author_id,"name":author.name}
    except sqlite3.InternalError:
        raise HTTPExeception(409,"Author name already exists")


@app.delete("/books",response_nodel=list[BookResponse])
def list_books():
    with get_connection() as conn:
        return [book_from_row(row)] for row in conn.execute("SELECT * FROM books ORDER BY id")











































