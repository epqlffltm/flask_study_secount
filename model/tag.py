from datetime import datetime
from pydantic import BaseModel

class tag_in(BaseModel):
    tag: str

class tag(BaseModel):
    tag:str
    created:datetime
    updated:str

class tag_out(BaseModel):
    tag:str
    created:datetime