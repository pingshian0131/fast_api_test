from fastapi import Query, FastAPI
from typing import List
from config import responses_products, tags_metadata
from models import Job
import logging
from jobs_web_crawler_104 import get_job
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight.theme": "tomorrow-night"},
    openapi_tags=tags_metadata,
)


@app.get(
    "/api/jobs/",
    summary="get products by ids passed by str splited by comma",
    responses=responses_products,
    response_model=List[Job],
    tags=["Job Finder"]
)
async def root(
    keywords: str = Query("python"),
):
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
