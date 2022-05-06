from models import (
    sample1_104, 
    sample2_104,
    sample1_1111,
    sample2_1111,
)

tags_metadata = [
    {
        "name": "Find Jobs From 104",
        "description": "從104人力銀行爬取要找的工作",
        "externalDocs": {
            "description": "104人力銀行",
            "url": "https://www.104.com.tw/jobs/main/"
        }
    },
    {
        "name": "Find Jobs From 1111",
        "description": "從1111人力銀行爬取要找的工作",
        "externalDocs": {
            "description": "1111人力銀行",
            "url": "https://www.1111.com.tw/"
        }
    }
]

responses_104 = {
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
                        "value": [sample1_104, sample2_104],
                    },
                    "id doesn't exist": {
                        "summary": "sample1_104 id can't find on 104 website",
                        "value": [{}, sample2_104],
                    }
                },
            },
        },
    },
}

responses_1111 = {
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
                        "value": [sample1_1111, sample2_1111],
                    },
                    "id doesn't exist": {
                        "summary": "sample1_1111 id can't find on 1111 website",
                        "value": [{}, sample2_1111],
                    }
                },
            },
        },
    },
}
