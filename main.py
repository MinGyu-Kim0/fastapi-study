from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/users/")
def read_users(q: str = Query(None, max_length=50)):
    return {"q": q}


@app.get("/items/")
def read_items(internal_query: str = Query(None, alias="search")):
    return {"query_handled": internal_query}


@app.get("/users2/")
def read_users(q: str = Query(None, deprecated=True)):
    return {"q": q}
