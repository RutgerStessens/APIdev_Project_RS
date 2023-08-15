from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime, timedelta
import jwt

app = FastAPI()

# OAuth2 Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Sample data for music genres, artists, albums, and songs
music_artists = [
    {"id": 1, "name": "Michael Jackson", "genre": "Pop"},
    {"id": 2, "name": "The Beatles", "genre": "Rock"},
    {"id": 3, "name": "Beyoncé", "genre": "R&B"},
]

music_albums = [
    {"id": 1, "title": "Thriller", "artist_id": 1},
    {"id": 2, "title": "Abbey Road", "artist_id": 2},
    {"id": 3, "title": "Lemonade", "artist_id": 3},
]

music_songs = [
    {"id": 1, "title": "Billie Jean", "album_id": 1},
    {"id": 2, "title": "Let It Be", "album_id": 2},
    {"id": 3, "title": "Formation", "album_id": 3},
]


class Artist(BaseModel):
    name: str
    genre: str


class Album(BaseModel):
    title: str
    artist_id: int


class Song(BaseModel):
    title: str
    album_id: int


# Dependency to get the current user based on the access token
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# OAuth2 token endpoint for user login
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Here you would perform user authentication, generate an access token,
    # and return it in the response.
    # ...


# GET - Get all artists (protected by OAuth)
@app.get("/artists", response_model=List[Artist])
async def get_music_artists(current_user: str = Depends(get_current_user)) -> List[Artist]:
    return music_artists


# GET - Get an artist and their albums (protected by OAuth)
@app.get("/artists/{artist_id}", response_model=Dict)
async def get_artist(artist_id: int, current_user: str = Depends(get_current_user)) -> Dict:
    # ...


# GET - Get a song and its album details (protected by OAuth)
@app.get("/songs/{song_id}", response_model=Dict)
async def get_song(song_id: int, current_user: str = Depends(get_current_user)) -> Dict:
    # ...


# GET - Get all albums with artist names (protected by OAuth)
@app.get("/albums", response_model=List[Dict])
async def get_music_albums(current_user: str = Depends(get_current_user)) -> List[Dict]:
    # ...


# POST - Add a new artist (protected by OAuth)
@app.post("/artists", response_model=Artist)
async def add_artist(artist: Artist, current_user: str = Depends(get_current_user)) -> Artist:
    # ...


# PUT - Update an album (protected by OAuth)
@app.put("/albums/{album_id}", response_model=Album)
async def update_album(album_id: int, album: Album, current_user: str = Depends(get_current_user)) -> Album:
    # ...


# DELETE - Delete a song (protected by OAuth)
@app.delete("/songs/{song_id}", response_model=Song)
async def delete_song(song_id: int, current_user: str = Depends(get_current_user)) -> Song:
    # ...


# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
