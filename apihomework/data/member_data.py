import json
import time
unquine = str(int(time.time()))
member_data = {
    "userid": "zhangsan" + unquine,
    "name": "zhangsan" + unquine,
    "alias": None,
    "mobile": "+86 " + unquine + "0",
    "department": [1],
    "order": [10],
    "position": None,
    "gender": "1",
    "email": "",
    "is_leader_in_dept": [0],
    "enable": 1,
    "avatar_mediaid": None,
    "telephone": "020-123456",
    "address": None,
    "main_department": 1,
    "extattr": {
        "attrs": [
            {
                "type": 0,
                "name": "文本名称",
                "text": {
                    "value": "文本"
                }
            },
            {
                "type": 1,
                "name": "网页名称",
                "web": {
                    "url": "http://www.test.com",
                    "title": "标题"
                }
            }
        ]
    },
    "to_invite": "false",
    "external_position": "高级产品经理",
    "external_profile": {
    }
}
print(member_data)
