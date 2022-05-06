from pydantic import BaseModel, Field, AnyUrl

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


sample1_104 = {
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
sample2_104 = {
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

sample1_1111 = {
    "date": "2022/05/03",
    "job_link": "https://www.1111.com.tw/job/77218137/",
    "title": "Python程式設計講師",
    "company_name": "社團法人新竹市職訓教育協會(經濟部IPAS能力鑑定認同機構、多益口說測驗-新竹考場,新竹職訓、智慧機械產業專業人才發展基地、榮獲)",
    "company_link": "https://www.1111.com.tw/corp/50960580/",
    "company_type": "協會╱基金會",
    "region": "新竹市東區",
    "seniority": "No data",
    "education": "No data",
    "content": "1. 結構業界實務經驗進行個案教學，讓學生與職場接軌\n2. 特定主題的專業領域，協助校內課程開課的豐富化\n3. 運用自身的專業知識與觀念提供諮詢服務\n4. 相關教材編寫\n5. 社會觀感及地位清高，易受社會大眾尊重\n6. 電腦應用教學\n7. 設計相關課程及開發課程\n8. 上課講義編寫\n9. 學員成果評估",
    "tags": "時薪 400~2,000元"
}

sample2_1111 = {
    "date": "2022/05/04",
    "job_link": "https://www.1111.com.tw/job/91477866/",
    "title": "(兼職工讀) Python 課程講師",
    "company_name": "藝派科技股份有限公司(核果資訊學苑)",
    "company_link": "https://www.1111.com.tw/corp/71626494/",
    "company_type": "其他教育服務業",
    "region": "苗栗縣竹南鎮",
    "seniority": "No data",
    "education": "No data",
    "content": "利用公司提供之教學內容與教材進行Python程式語言授課。須於正式授課前接受公司培訓，確認教學技巧與教材之正確使用。\n\n亦歡迎教師就自身專長帶領學員進行進階主題專案之製作，此類課程教材由教師自編。",
    "tags": "時薪 700~1,000元"
}
