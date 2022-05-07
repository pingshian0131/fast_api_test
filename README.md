# FastAPI Demo
<hr>

* Documentation: <br>
> * [FastAPI Documentation](https://fastapi.tiangolo.com/ "FastAPI Documentation")<br>
> * [Requests Documentation](https://docs.python-requests.org/en/latest/ "Requests Documentation")<br>
> * [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/ "Beautiful Soup Documentation")<br>

* Intro
> * combine web_crawler and FastAPI <br>
> * web_crawler use `requests` and `BeautifulSoup` on 104人力銀行、1111人力銀行 website.<br>
> * FastAPI variables explanation <br>

<hr>

# Start
`uvicorn main:app --reload --port 8001`

* FastAPI 預設的 port 是 8000，因為跟 Django 衝到才改成 8001，平時不用加 --port 的參數

# Swagger UI link:
`http://127.0.0.1:8001/docs`
![](https://github.com/pingshian0131/fast_api_test/raw/main/static/docs_pic.png)

`http://127.0.0.1:8001/redoc`
![](https://github.com/pingshian0131/fast_api_test/raw/main/static/redoc_pic.png)

# detail

* title and category <br>
[Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/ "Metadata and Docs URLs")<br>
[Configuring Swagger UI - Change the Theme](https://fastapi.tiangolo.com/advanced/extending-openapi/#change-the-theme "Configuring Swagger UI - Change the Theme")<br>
![](https://github.com/pingshian0131/fast_api_test/raw/main/static/title&category.png)


* variables
  * set the api's header data: <br>
[Response Model](https://fastapi.tiangolo.com/tutorial/response-model/ "Response Model")<br>
[Summary and description](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#summary-and-description "Summary and description")<br>
[Create metadata for tags](https://fastapi.tiangolo.com/tutorial/metadata/#create-metadata-for-tags "Create metadata for tags")<br>
```
@app.get(
    "/api/jobs/104/",
    summary="get jobs list from 104 by keywords",
    description="從104人力銀行爬取要找的工作",
    responses=responses_104,
    response_model=List[Job],
    tags=["Job Finder From 104"]
)
# responses_104, responses_1111 in config.py used to set samples when status_code == 200 and 204,
# can add other http status_code if you want
```
  * params input: <br>
[Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/ "Query Parameters")<br>
[Additional validation](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/ "Additional validation")<br>
```
async def root(
    keywords: str = Query("python", max_length=10),
):
# url will be http://127.0.0.1:8001/api/jobs/104/?keywords=python
```
  * return value validation: <br>
[Body - Fields](https://fastapi.tiangolo.com/tutorial/body-fields/ "Body - Fields")<br>
```
# same as FinMind, use pydantic
# models.py
class Job(BaseModel):
    date: str = Field(title="更新日期")
    job_link: AnyUrl = Field(title="工作網址")
    title: str = Field(title="職稱")
    company_name: str = Field(title="公司")
    company_link: str = Field(title="公司網址")
    company_type: str = Field(title="公司產業")
    region: str = Field(title="地區")
    seniority: str = Field(title="年資")
    education: str = Field(title="學歷")
    content: str = Field(title="工作內容")
    tags: str = Field(title="其他標籤")
```
  * return value: <br>
[JSON Compatible Encoder](https://fastapi.tiangolo.com/tutorial/encoder/ "JSON Compatible Encoder")<br>
[Return a Response Directly](https://fastapi.tiangolo.com/advanced/response-directly/ "Return a Response Directly")<br>
```
async def query_1111(
    keywords: str = Query("python", max_length=10),
):
    res = get_jobs_from_1111(keywords=keywords)
    json_compatible_item_data = jsonable_encoder(res)
    return JSONResponse(content=json_compatible_item_data)
```
