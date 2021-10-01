from fastapi import FastAPI, HTTPException, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel
from api.SmartBookmark import evaluateText, evaluateUrl, labels
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HypeLinks API: A Smart Bookmark API",
    version="1.0.0-beta02",
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


@app.get("/status")
async def index():
    return {"status": "online"}


@app.get("/list")
async def index():
    return {
        "categories": [{"category_id": k, "category": v} for k, v in labels.items()]
    }


class InputUrl(BaseModel):
    url: str


class InputText(BaseModel):
    text: str


@app.post("/classify/url")
async def get_item(input: InputUrl):
    try:
        title, test_preds = evaluateUrl(input.url)
        return {
            "url": input.url,
            "title": title[0],
            "category": test_preds,
            "category_id": id,
        }
    except:
        raise HTTPException(status_code=400, detail="Enter a valid URL!")


@app.post("/classify/text")
async def get_item(input: InputText):
    try:
        title, test_preds, id = evaluateText([input.text])
        return {"title": title[0], "category": test_preds, "category_id": id}
    except:
        raise HTTPException(status_code=400, detail="Error")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
