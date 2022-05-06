from models import sample1, sample2

blank_img_url = "https://tholiday.thsrc.com.tw/agts_thw/img/list_img_blank.jpg"

tags_metadata = [
    {
        "name": "Job Finder",
        "description": "爬取要找的工作",
        "externalDocs": {
            "description": "104人力銀行",
            "url": "https://www.104.com.tw/jobs/main/"
        }
    },
    {
        "name": "",
        "description": "456",
        "externalDocs": {
            "description": "104人力銀行",
            "url": "https://www.104.com.tw/jobs/main/"
        }
    }
]

responses_products = {
    "204": {
        "content": {
            "application/json": {
                "example": [{}, {}],
                "schema": {
                    "title": "empty list",
                    "type": "array",
                },
            },
        },
        "description": "Item not found",
    },
    "200": {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "examples": {
                    "normal": {
                        "summary": "normal example",
                        "value": [sample1, sample2],
                    },
                    "id doesn't exist": {
                        "summary": "sample1 id can't find on thsrcholiday website",
                        "value": [{}, sample2],
                    }
                },
            },
        },
    },
}
