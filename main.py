from fastapi import FastAPI
from fastapi import Body
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

@app.post('/movies', tags=['movies'])
def create_movie(id:int=Body(), title:str=Body(), overview:str=Body(), year:int=Body(), rating:float=Body(), category:str=Body()):
    movies.append({
        'id':id,
        'title':title,
        'overview':overview,
        'year':year,
        'rating':rating,
        'category':category
    })
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id:int, title:str=Body(), overview:str=Body(), year:int=Body(), rating:float=Body(), category:str=Body()):
    for item in movies:
        if item['id'] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category
            return movies

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id:int, title:str=Body(), overview:str=Body(), year:int=Body(), rating:float=Body(), category:str=Body()):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies