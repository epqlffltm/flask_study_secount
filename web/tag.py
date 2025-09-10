from datetime import datetime
from model.tag import tag,tag_in,tag_out
import service.tag as service
from fastapi import FastAPI

app=FastAPI()

@app.post("/")
def create_tag(tag_in:tag_out)->tag_in:
    tag: tag=tag(tag=tag_in.tag,created=datetime.utcnow(),secret="shhhh")
    service.create(tag)
    return tag_in

@app.get("/{tag_str}",response_model=tag_out)
def get_one(tag_str:str)->tag_out:
    tag:tag=service.get(tag_str)
    return tag