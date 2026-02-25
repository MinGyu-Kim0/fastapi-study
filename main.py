from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/greet")
def greeting(request: Request, time_of_day: str):
    return templates.TemplateResponse(
        "index.html", {"request": request, "time_of_day": time_of_day}
    )
