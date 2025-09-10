from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# ===================
# 모델 정의
# ===================
class TagIn(BaseModel):
    tag: str

class Tag(BaseModel):
    tag: str
    created: datetime
    updated: str = ""

class TagOut(BaseModel):
    tag: str
    created: datetime

# ===================
# 서비스 함수
# ===================
tags_storage = {}  # 간단한 메모리 저장용 dict

def create_tag_service(tag_obj: Tag):
    tags_storage[tag_obj.tag] = tag_obj
    return tag_obj

def get_tag_service(tag_str: str):
    return tags_storage.get(tag_str) or Tag(tag=tag_str, created=datetime.utcnow())

# ===================
# 라우터
# ===================
@app.post("/", response_model=TagOut)
def create_tag(tag_in: TagIn):
    tag_obj = Tag(tag=tag_in.tag, created=datetime.utcnow())
    create_tag_service(tag_obj)
    return TagOut(tag=tag_obj.tag, created=tag_obj.created)

@app.get("/{tag_str}", response_model=TagOut)
def get_tag(tag_str: str):
    tag_obj = get_tag_service(tag_str)
    return TagOut(tag=tag_obj.tag, created=tag_obj.created)


'''from fastapi import FastAPI,Header
import uvicorn
app=FastAPI()
@app.get("/hi")
def index(who:str=Header()):
    return f"{who}"

@app.get("/hi")
def hi():
    return [{"message": "Hello python"},{"message": "Hello fastAPI"}]

@app.get("/{user}")
def user(user):
    return f"Hello {user}"

@app.get("/hi")
def greet(who:str=Body(embed=True)):   # ← 인자 이름을 쿼리파라미터 이름과 동일하게!
    return f"Hello {who}"


if __name__=='__main__':
    uvicorn.run("app:app", reload=True)'''