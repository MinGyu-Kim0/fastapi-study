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


@app.get("/items2/")
def read_items(
    string_query: str = Query(
        default="default value",
        min_length=2,
        max_length=5,
        regex="^[a-zA-Z]+$",
        title="String Query",
        example="abc",
    ),
    number_query: float = Query(
        default=1.0, ge=0.5, le=10.5, title="Number Query", example=5.5
    ),
):
    return {"string_query_handled": string_query, "number_query_handled": number_query}
