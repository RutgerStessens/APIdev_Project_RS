# Music API Documentation

Welcome to my documentation for **My Music Library API**. This API allows you to manage information about music genres, artists, albums, and songs. You can interact with the API using HTTP requests to perform various actions on your music library.

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
- [Running the API](#running-the-api)
- [Examples](#examples)

## Introduction

My Music Library API provides endpoints for interacting with music genres, artists, albums, and songs. This API is built using the FastAPI framework and utilizes SQLAlchemy for database management.

## Endpoints

### Get All Artists

**Endpoint:** `GET /artists`

Retrieves a list of all music artists in the library.

### Get Artist and Albums

**Endpoint:** `GET /artists/{artist_id}`

Retrieves detailed information about a specific artist, including their albums.

### Get Song and Album Details

**Endpoint:** `GET /songs/{song_id}`

Retrieves detailed information about a specific song, including the album it belongs to and the artist.

### Get All Albums with Artist Names

**Endpoint:** `GET /albums`

Retrieves a list of all albums in the library, along with the names of their respective artists.

### Add a New Artist

**Endpoint:** `POST /artists`

Adds a new artist to the music library. Requires providing the artist's name and genre in the request.

### Update an Album

**Endpoint:** `PUT /albums/{album_id}`

Updates the details of an existing album. Requires providing the new title and artist ID in the request.

### Delete a Song

**Endpoint:** `DELETE /songs/{song_id}`

Deletes a song from the music library.

## Data Models

The API's data is structured using the following data models:

### Artist

- `id`: Unique identifier for the artist
- `name`: Name of the artist
- `genre`: Genre of the artist's music

### Album

- `id`: Unique identifier for the album
- `title`: Title of the album
- `artist_id`: ID of the artist associated with the album

### Song

- `id`: Unique identifier for the song
- `title`: Title of the song
- `album_id`: ID of the album to which the song belongs

## Database Setup

The API uses an SQLite database for storing music library data. Tables for artists, albums, and songs are automatically created when the application starts.


## Running the API

You can run the API using the following command:

```bash
uvicorn main:app --reload
