# Music Library API Documentation

Welcome to the documentation for the **Music Library API**. This API allows you to manage information about music artists, albums, and songs. You can interact with the API using HTTP requests.

## Table of Contents

- [Introduction](#introduction)
- [Endpoints](#endpoints)
  - [Get All Artists](#get-all-artists)
  - [Get Artist and Albums](#get-artist-and-albums)
  - [Get Song and Album Details](#get-song-and-album-details)
  - [Get All Albums with Artist Names](#get-all-albums-with-artist-names)
  - [Add a New Artist](#add-a-new-artist)
  - [Update an Album](#update-an-album)
  - [Delete a Song](#delete-a-song)
- [Data Models](#data-models)
- [Database Setup](#database-setup)

## Introduction

The Music Library API provides endpoints to interact with music genres, artists, albums, and songs. It is built using the FastAPI framework and SQLAlchemy for database management.

## Endpoints

### Get All Artists

Endpoint: `GET /artists`

Retrieve a list of all music artists.

### Get Artist and Albums

Endpoint: `GET /artists/{artist_id}`

Retrieve information about a specific artist, including their albums.

### Get Song and Album Details

Endpoint: `GET /songs/{song_id}`

Retrieve details about a specific song, including the album it belongs to and the artist.

### Get All Albums with Artist Names

Endpoint: `GET /albums`

Retrieve a list of all albums along with the names of their respective artists.

### Add a New Artist

Endpoint: `POST /artists`

Add a new artist to the music library. Provide the artist's name and genre in the request.

### Update an Album

Endpoint: `PUT /albums/{album_id}`

Update the details of an existing album. Provide the new title and artist ID in the request.

### Delete a Song

Endpoint: `DELETE /songs/{song_id}`

Delete a song from the music library.

## Data Models

The following data models are used to structure the API's data:

### Artist

- `id`: Artist's unique identifier
- `name`: Artist's name
- `genre`: Artist's genre

### Album

- `id`: Album's unique identifier
- `title`: Album's title
- `artist_id`: ID of the artist associated with the album

### Song

- `id`: Song's unique identifier
- `title`: Song's title
- `album_id`: ID of the album the song belongs to

## Database Setup

The API uses an SQLite database for storing music library data. The SQLAlchemy library is used for database management.

The database setup is performed automatically. Tables are created for artists, albums, and songs when the application starts.

Please note that this is a basic documentation overview. For more detailed information and examples of how to use each endpoint, refer to the API implementation.
