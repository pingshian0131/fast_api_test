from typing import List, Dict
from pydantic import BaseModel, Field, AnyUrl
from datetime import date


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


sample1 = {
    "date": "5/05",
    "job_link": "https://www.104.com.tw/job/79ufi?jobsource=jolist_a_relevance",
    "title": "Python Engineer",
    "company_name": "安智聯科技有限公司",
    "company_link": "https://www.104.com.tw/company/1a2x6bkzzz?jobsource=jolist_a_relevance",
    "company_type": "電腦軟體服務業",
    "region": "桃園市桃園區",
    "seniority": "3年以上",
    "education": "大學",
    "content": "1. 負責搭建和持續改進項目平台\n2. 負責數據分析平台開發與優化\n3. 持續提升團隊工程效率，探索符合團隊特色的工作流\n\n需求條件：\n- 熟悉開發 Restful API\n- 有MySQL、MongoDB、PostgreSQL 等使用經驗\n- 對代碼和設計質量嚴格要求，重視Code Review，有良好的開發習慣\n- 熟悉 Linux 基本常見指令\n- 熟悉常用算法和數據結構與網路知識\n- 熟悉git版本管理",
    "tags": "月薪45,000元以上,員工20人"
}
sample2 = {
    "date": "5/05",
    "job_link": "https://www.104.com.tw/job/5z6t9?jobsource=jolist_a_relevance",
    "title": "Python Engineer (松山區)",
    "company_name": "億力資訊股份有限公司",
    "company_link": "https://www.104.com.tw/company/bjvssxk?jobsource=jolist_a_relevance",
    "company_type": "電腦軟體服務業",
    "region": "台北市松山區",
    "seniority": "經歷不拘",
    "education": "高中",
    "content": "1.具備Python實務專案經驗\n2.有AWS的2年經驗\n3.倉儲系統開發\n4.主動性強、樂與團隊互動討論\n5.須配合客戶端駐點\n",
    "tags": "待遇面議,員工180人"
}
