import requests
from bs4 import BeautifulSoup
from ..models import Job
import re


def get_jobs(keywords="python"):
    res = []
    link = f"https://www.1111.com.tw/search/job?ks={keywords}"
    r = requests.get(link)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        articles = soup.find_all(class_="item__job")

        for article in articles:
            date = article.find(class_="job_item_date").text
            job_link = article.find("a").get("href")
            title = article.find("h5").text

            company_detail = article.find(class_="card-subtitle").find("a").get("title").split("\r\n")

            company_name = article.find(class_="job_item_company").text
            company_link = article.find(class_="card-subtitle").find("a").get("href")
            try:
                company_type = re.search("》(.*?)$", company_detail[1]).group(1)
            except IndexError:
                company_type = ""
            region = article.find(class_="job_item_detail_location").text
            seniority = "No data"
            education = "No data"
            content = article.find(class_="job_item_description").text

            tags = article.find(class_="job_item_detail_salary").text


            res.append(
                Job(
                    date=date,
                    job_link=job_link,
                    title=title,
                    company_name=company_name,
                    company_link=company_link,
                    company_type=company_type,
                    region=region,
                    seniority=seniority,
                    education=education,
                    content=content,
                    tags=tags,
                )
            )
        return res
