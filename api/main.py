from fastapi import FastAPI, HTTPException, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel
from api.SmartBookmark import evaluate, labels
import azure.functions as func
from api.http_asgi import AsgiMiddleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Smart Bookmark",
    version="1.0",
    description="Classifies the sites into various different categories",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
        "http://0.0.0.0:8000",
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:3000",
        "http://localhost:0000",
        "http://smart-bookmark-api.iamyajat.co",
        "https://smart-bookmark-api.iamyajat.co",
        "http://smart-bookmark-api.azurewebsites.net",
        "https://smart-bookmark-api.azurewebsites.net",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Access-Control-Allow-Origin", "*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request, "id": 1})


@app.get("/list")
async def index():
    return {"categories": [v for k, v in labels.items()]}


class Input(BaseModel):
    url: str


@app.post("/classify")
async def get_item(input: Input):
    try:
        title, test_preds = evaluate(input.url)
        return {"title": title[0], "category": test_preds}
    except:
        raise HTTPException(status_code=400, detail="Enter a valid URL!")


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5000)
