from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()


@app.get("/items/")
# 타입은 List이어야 하고 각각의 요소는 int형이어야 함. List타입 힌트는 Query와 반드시 같이 사용해야함.
async def read_items(q: List[int] = Query([])):
    return {"q": q}


@app.post("/create-item/")
async def create_item(item: Dict[str, int]):
    return item


# 실행: uvicorn main:app --reload
