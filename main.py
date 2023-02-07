from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()     #To run use uvicorn main:app --reload
app.title = 'FastAPI app'
app.version = '1.0'

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id:int):
    movie = list(filter(lambda x: x['id'] == id,movies))
    return movie if len(movie) > 0 else "There are no movies in list"

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str):
    return [movie for movie in movies if movie['category'] == category]
