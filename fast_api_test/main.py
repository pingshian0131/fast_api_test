from fastapi import Query, FastAPI
from typing import List
from config import responses_products, tags_metadata
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import Job
from .utils.get_jobs_from_104 import get_jobs
import logging
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
    summary="get jobs list from 104 by keywords",
    responses=responses_products,
    response_model=List[Job],
    tags=["Job Finder"]
)
async def root(
    keywords: str = Query("python"),
):
    res = get_jobs(keywords=keywords)
    json_compatible_item_data = jsonable_encoder(res)
    return JSONResponse(content=json_compatible_item_data)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
