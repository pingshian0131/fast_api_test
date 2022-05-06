# FastAPI Demo
<hr>

* combine web_crawler and FastAPI <br>

* web_crawler use `requests` and `BeautifulSoup` on 104人力銀行、1111人力銀行 website.<br>

* FastAPI variables explanation <br>

<hr>

# Start
`python -m uvicorn main.py:app --reload --port 8001`

* FastAPI 預設的 port 是 8000，因為跟 Django 衝到才改成 8001，平時不用加 --port 的參數

# Swagger UI link:
`http://127.0.0.1:8001/docs`
![](https://github.com/pingshian0131/fast_api_test/raw/main/static/docs_pic.png)

`http://127.0.0.1:8001/redoc`
![](https://github.com/pingshian0131/fast_api_test/raw/main/static/redoc_pic.png)

# detail

* title and category
![](https://github.com/pingshian0131/fast_api_test/raw/main/static/title&category.png)


* variables
  * set the api's header data
```
@app.get(
    "/api/jobs/104/",
    summary="get jobs list from 104 by keywords",
    responses=responses_104,
    response_model=List[Job],
    tags=["Job Finder From 104"]
)
# responses_104, responses_1111 in config.py used to set samples when status_code == 200 and 204,
# can add other http status_code if you want
```
  * params input
```
async def root(
    keywords: str = Query("python"),
):
# url will be http://127.0.0.1:8001/api/jobs/104/?keywords=python
```
  * return value validation
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


