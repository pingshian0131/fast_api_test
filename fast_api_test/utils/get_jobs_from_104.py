from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup
import sys
from ..models import Job

def get_jobs(keyword="python"):
    res = []
    link = f"https://www.104.com.tw/jobs/search/?ro=1&keyword={keyword}&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&page=1&mode=s&jobsource=2018indexpoc"
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
            company_type = job_detail[0].find_all("li")[2].text
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
                    tags=tags,
                )
            )



class job():
    def __init__(self, date, url, title, company, company_url, company_type, region, seniority, education, required, tags):
#        for k, v in kwargs.items():
#            print(k, v)
#            k=v
        self.date = date 
        self.url = url
        self.title = title
        self.company = company
        self.company_url = company_url
        self.company_type = company_type
        self.region = region
        self.seniority = seniority
        self.education = education
        self.required = required
        self.tags = tags

    def iter(self):
        print("date: {}".format(self.date))
        print("url: {}".format(self.url))
        print("title: {}".format(self.title))
        print("company: {}".format(self.company))
        print("company_url: {}".format(self.company_url))
        print("company_type: {}".format(self.company_type))
        print("region: {}".format(self.region))
        print("seniority: {}".format(self.seniority))
        print("education: {}".format(self.education))
        print("required: {}".format(self.required))
        print("tags: {}".format(self.tags))
        print()
        print()
        print()

def main():
    chrome_options = webdriver.ChromeOptions()
#    chrome_options.add_argument('--headless')
#    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    
    driver.get('https://www.104.com.tw/jobs/search/?ro=1&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&page=1&mode=s&jobsource=2018indexpoc')
    "https://www.104.com.tw/jobs/search/?ro=1&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=14&asc=0&page=1&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    "https://www.104.com.tw/jobs/search/?ro=1&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000%2C6001002000&order=14&asc=0&page=1&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    for i in range(11,18,1):
        print("******第 {} 個*******".format(i))
        a = driver.find_element_by_xpath('//*[@id="js-job-content"]/article['+str(i)+']')
    #   a.data: //*[@id="js-job-content"]/article[11]/div[1]
    #    a.data.date: //*[@id="js-job-content"]/article[11]/div[1]/h2/span
    #    a.data.title: //*[@id="js-job-content"]/article[11]/div[1]/h2/a (include href
    #    a.data.company: //*[@id="js-job-content"]/article[11]/div[1]/ul[1]/li[2]/a (include href
    #    a.data.company.type: //*[@id="js-job-content"]/article[11]/div[1]/ul[1]/li[3]
    #    a.data.region: //*[@id="js-job-content"]/article[11]/div[1]/ul[2]/li[1]
    #    a.data.seniority: //*[@id="js-job-content"]/article[11]/div[1]/ul[2]/li[2]
    #    a.data.education: //*[@id="js-job-content"]/article[11]/div[1]/ul[2]/li[3]
    #    a.data.required: //*[@id="js-job-content"]/article[11]/div[1]/p
    #    a.data.salary: //*[@id="js-job-content"]/article[11]/div[1]/div/span[1]
    #    a.data.staff: //*[@id="js-job-content"]/article[11]/div[1]/div/span[2]
    #    a.data.landmark: //*[@id="js-job-content"]/article[11]/div[1]/div/span[3]
        data = a.find_element_by_xpath('./div[1]')
        date = data.find_element_by_xpath('./h2/span').get_attribute('innerHTML').replace('\n','').replace(' ','')
        url = data.find_element_by_xpath('./h2/a').get_attribute('href')
        title = data.find_element_by_xpath('./h2/a').get_attribute('innerHTML').replace('<em class="b-txt--highlight">','').replace('</em>','')
        company = data.find_element_by_xpath('./ul[1]/li[2]/a').get_attribute('innerHTML').replace('\n','').replace(' ','')
        company_url = data.find_element_by_xpath('./ul[1]/li[2]/a').get_attribute('href')
        company_type = data.find_element_by_xpath('./ul[1]/li[3]').get_attribute('innerHTML')
        region = data.find_element_by_xpath('./ul[2]/li[1]').get_attribute('innerHTML')
        seniority = data.find_element_by_xpath('./ul[2]/li[2]').get_attribute('innerHTML')
        education = data.find_element_by_xpath('./ul[2]/li[3]').get_attribute('innerHTML')
        required = data.find_element_by_xpath('./p').get_attribute('innerHTML').replace('<em class="b-txt--highlight">','').replace('</em>','')
        tags = data.find_element_by_xpath('./div').get_attribute('innerHTML').replace('\n','').replace('<span class="b-tag--default">','').replace('</span>',', ').replace(' ','')
    
        a = job(
            date=date,
            url=url,
            title=title,
            company=company,
            company_url=company_url,
            company_type=company_type,
            region=region,
            seniority=seniority,
            education=education,
            required=required,
            tags=tags)
        a.iter()
    input()
    sys.exit()


if __name__ == '__main__':
    main()
