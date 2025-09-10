from datetime import datetime
from model.tag import tag

def create(tag: tag)->tag:
    return tag

def get(tag_str:str)->tag:
    return tag(tag=tag_str,created=datetime.utcnow(),secret="")