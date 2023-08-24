from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from datetime import datetime, timedelta
from typing import Dict, List

from .auth import authenticate_user
from .models import Artist, Album, Song

app = FastAPI()

# OAuth2 setup
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Data (your sample data here)
music_artists = [
    {"id": 1, "name": "Pendulum", "genre": "Drum and Bass"},
    {"id": 2, "name": "Netsky", "genre": "Drum and Bass"},
    {"id": 3, "name": "Andy C", "genre": "Drum and Bass"},
]

music_albums = [
    {"id": 1, "title": "Hold Your Colour", "artist_id": 1},
    {"id": 2, "title": "2", "artist_id": 2},
    {"id": 3, "title": "Nightlife 5", "artist_id": 3},
]

music_songs = [
    {"id": 1, "title": "Tarantula", "album_id": 1},
    {"id": 2, "title": "Rio", "album_id": 2},
    {"id": 3, "title": "Heartbeat Loud", "album_id": 3},
    {"id": 4, "title": "Watercolour", "album_id": 1},
    {"id": 5, "title": "Come Alive", "album_id": 2},
    {"id": 6, "title": "Workout", "album_id": 3},
]
# Endpoints
@app.get("/albums", response_model=List[Dict])
async def get_music_albums() -> List[Dict]:
    albums_with_artists = []
    for album in music_albums:
        artist_id = album["artist_id"]
        artist = next((a for a in music_artists if a["id"] == artist_id), None)
        if artist:
            album["artist_name"] = artist["name"]
        albums_with_artists.append(album)
    return albums_with_artists

@app.get("/artists", response_model=List[Artist])
async def get_music_artists() -> List[Artist]:
    return music_artists

@app.get("/songs", response_model=List[Song])
async def get_all_songs() -> List[Song]:
    return music_songs

@app.post("/artists", response_model=Artist)
async def add_artist(artist: Artist) -> Artist:
    new_artist = {"id": len(music_artists) + 1, "name": artist.name, "genre": artist.genre}
    music_artists.append(new_artist)
    return new_artist

@app.post("/songs", response_model=Song)
async def add_song(song: Song) -> Song:
    new_song = {"id": len(music_songs) + 1, "title": song.title, "album_id": song.album_id}
    music_songs.append(new_song)
    return new_song

@app.put("/albums/{album_id}", response_model=Album)
async def update_album(album_id: int, album: Album) -> Album:
    album_index = next((index for index, a in enumerate(music_albums) if a["id"] == album_id), None)
    if album_index is None:
        raise HTTPException(status_code=404, detail="Album not found")
    music_albums[album_index]["title"] = album.title
    music_albums[album_index]["artist_id"] = album.artist_id
    return music_albums[album_index]

@app.put("/songs/{song_id}", response_model=Song)
async def update_song(song_id: int, updated_song: Song) -> Song:
    song_index = next((index for index, s in enumerate(music_songs) if s["id"] == song_id), None)
    if song_index is None:
        raise HTTPException(status_code=404, detail="Song not found")
    music_songs[song_index]["title"] = updated_song.title
    music_songs[song_index]["album_id"] = updated_song.album_id
    return music_songs[song_index]

@app.delete("/songs/{song_id}", response_model=Song)
async def delete_song(song_id: int) -> Song:
    song = next((s for s in music_songs if s["id"] == song_id), None)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    music_songs.remove(song)
    return song

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
