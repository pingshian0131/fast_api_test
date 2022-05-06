import requests
from bs4 import BeautifulSoup
from ..models import Job
import re


def get_jobs_from_104(keywords="python"):
    res = []
    link = f"https://www.104.com.tw/jobs/search/?ro=1&keyword={keywords}&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&page=1&mode=s&jobsource=2018indexpoc"
    r = requests.get(link)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        data = soup.find(id="js-job-content")
        articles = data.find_all("article")

        for article in articles:
            date = article.find("h2").find("span").text.replace(" ", "")
            job_link = "https:" + article.find("h2").find("a").get("href")
            title = article.find("h2").find("a").text

            job_detail = article.find_all("ul")
            company_name = job_detail[0].find("a").text.replace("\n", "").replace(" ", "")
            company_link = "https:" + job_detail[0].find("a").get("href")
            try:
                company_type = job_detail[0].find_all("li")[2].text
            except IndexError:
                company_type = ""
            region = job_detail[1].find_all("li")[0].text
            seniority = job_detail[1].find_all("li")[1].text
            education = job_detail[1].find_all("li")[2].text
            content = article.find("p").text.replace("\r", "")

            tags_data = article.find_all(class_="b-tag--default")
            tags = [tag.text for tag in tags_data]


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
                    tags=",".join(tags),
                )
            )
        return res


def get_jobs_from_1111(keywords="python"):
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
