# My Music Library API Documentation

Welcome to the documentation for **My Music Library API**. This API allows me to manage information about music genres, artists, albums, and songs. I can interact with the API using HTTP requests.

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

My Music Library API provides endpoints for me to interact with music genres, artists, albums, and songs. I've built this API using the FastAPI framework and SQLAlchemy for database management.

## Endpoints

### Get All Artists

**Endpoint:** `GET /artists`

I can retrieve a list of all music artists.

### Get Artist and Albums

**Endpoint:** `GET /artists/{artist_id}`

I can retrieve information about a specific artist, including their albums.

### Get Song and Album Details

**Endpoint:** `GET /songs/{song_id}`

I can retrieve details about a specific song, including the album it belongs to and the artist.

### Get All Albums with Artist Names

**Endpoint:** `GET /albums`

I can retrieve a list of all albums along with the names of their respective artists.

### Add a New Artist

**Endpoint:** `POST /artists`

I can add a new artist to my music library. I need to provide the artist's name and genre in the request.

### Update an Album

**Endpoint:** `PUT /albums/{album_id}`

I can update the details of an existing album. I need to provide the new title and artist ID in the request.

### Delete a Song

**Endpoint:** `DELETE /songs/{song_id}`

I can delete a song from my music library.

## Data Models

I've structured my API's data using the following data models:

### Artist

- `id`: The artist's unique identifier
- `name`: The artist's name
- `genre`: The artist's genre

### Album

- `id`: The album's unique identifier
- `title`: The album's title
- `artist_id`: The ID of the artist associated with the album

### Song

- `id`: The song's unique identifier
- `title`: The song's title
- `album_id`: The ID of the album the song belongs to

## Database Setup

My API uses an SQLite database for storing music library data. I've leveraged the SQLAlchemy library for database management.

The database setup occurs automatically when the application starts. Tables are created for artists, albums, and songs.

Please note that this is a basic overview of my documentation. For more in-depth information and examples on how to use each endpoint, refer to my API's implementation.
