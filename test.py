from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pytubefix import YouTube
from pytubefix.cli import on_progress

class Song(BaseModel):
    url: str

app = FastAPI()

@app.post("/song")
def get_song(song: Song):
    try:
        yt = YouTube(song.url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        return {"name" : yt.title}
    except:
        raise HTTPException(400, "Song URL was not found on youtube.")
