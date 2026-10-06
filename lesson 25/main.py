from fastapi import FastAPI, HTTPException
from typing import List

import database
import models
from models import  Movies,MoviesCreate



app = FastAPI()

@app,get("/")
def read_root():
    return {"message":"Welcome to the movies Crud API"}

@app.get("/movies",response_model=Movie)
def create_movie(movie: MoviesCreate):
    movie_id = database.create_movie(movie)
    return model.Movie(id=movie_id, **movie.dict())




