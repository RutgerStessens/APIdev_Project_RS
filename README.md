# Music API Documentation

Welcome to the documentation of the Music API! This API allows you to interact with a database containing information about music artists, albums, and songs.

## Getting Started

To get started using the Music API, you need to have Python and FastAPI installed on your system. Additionally, you'll need the SQLite database engine.

1. Install dependencies:
pip install fastapi
pip install uvicorn
pip install sqlalchemy

3. Start the FastAPI server:
uvicorn main:app --host 0.0.0.0 --port 8000


## Endpoints

### Authentication

Before using the API endpoints, you need to authenticate to get an access token. Use the `/token` endpoint to obtain an access token by providing your username and password. This access token will be required for subsequent requests.

### Available Endpoints

- **GET /artists**
- Description: Get a list of all music artists.
- Authentication: Required
- Response: List of artist objects containing id, name, and genre.

- **GET /artists/{artist_id}**
- Description: Get detailed information about a specific artist including their albums.
- Authentication: Required
- Parameters: artist_id (int) - ID of the artist.
- Response: Artist object containing id, name, genre, and albums.

- **GET /songs/{song_id}**
- Description: Get information about a specific song including its album and artist.
- Authentication: Required
- Parameters: song_id (int) - ID of the song.
- Response: Song details object containing song, album, and artist information.

- **GET /albums**
- Description: Get a list of all albums with associated artist names.
- Authentication: Required
- Response: List of album objects containing id, title, artist_id, and artist_name.

- **POST /artists**
- Description: Add a new artist to the database.
- Authentication: Required
- Request Body: Artist object containing name and genre.
- Response: New artist object with generated id.

- **PUT /albums/{album_id}**
- Description: Update an existing album's title and artist.
- Authentication: Required
- Parameters: album_id (int) - ID of the album.
- Request Body: Album object containing title and artist_id.
- Response: Updated album object.

- **DELETE /songs/{song_id}**
- Description: Delete a song from the database.
- Authentication: Required
- Parameters: song_id (int) - ID of the song.
- Response: Deleted song object.

## Security

This API uses OAuth2 authentication to secure endpoints. You need to obtain an access token using the `/token` endpoint and include it in the `Authorization` header of your requests.

## Data Model

The API is based on three main entities:

- **Artist**: Represents a music artist with attributes id, name, genre, and albums.
- **Album**: Represents an album with attributes id, title, artist_id, and songs.
- **Song**: Represents a song with attributes id, title, and album_id.

## Notes

- This API is designed for educational purposes and may not include all security measures required for production environments.
- Replace "your-secret-key" with an actual secret key for token generation.
