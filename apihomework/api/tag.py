import time

import requests
from api.base_api import BaseApi
"""
1.测试接口放到类中，可以让其他方法进行复用
2.便于统一处理，重复逻辑可以提取复用
3.建议把必填参数放到函数的参数中，非必填放到kwargs中
4.把base url封装到父类中
"""


class TagApi(BaseApi):
    def create_tag(self, data=None):
        # 创建标签
        token = self.token
        url = self._URL + f"/tag/create?access_token={token}"
        if data is None:
            data = {
                "tagname": "tagname" + str(time.time()),
                "tagid": int(time.time())
            }
        return requests.post(url, json=data)

    def delete_tag(self, tagid=None):
        token = self.token
        # 通过tagid删除标签
        if tagid is None:
            tagid = int(time.time())
        delete_data = {
            "tagname": "tagname" + str(time.time()),
            "tagid": tagid
        }
        self.create_tag(delete_data)
        url = self._URL + f"/tag/delete?access_token={token}&tagid={delete_data.get('tagid')}"
        return requests.get(url)

    def update_tag(self, name=None):
        token = self.token
        # 更新tagname
        if name is None:
            name = "tagname" + str(time.time())
        create_data = {
            "tagname": "tagname" + str(time.time()),
            "tagid": int(time.time())
        }
        self.create_tag(create_data)

        url = self._URL + f"/tag/update?access_token={token}"
        update_data = {
            "tagid": create_data.get("tagid"),
            "tagname": name
        }
        return requests.post(url, json=update_data)

    def get_tag_list(self):
        # 获取标签列表
        token = self.token
        url = self._URL + f'/tag/list?access_token={token}'
        return requests.get(url)

    def get_tag_name_list(self):
        # 获取所有tagname
        taglist = self.get_tag_list().json().get('taglist')
        tagname_list = []
        for i in range(len(taglist)):
            tagname_list.append(taglist[i].get('tagname'))
        return tagname_list

    def get_tag_id_list(self):
        # 获取所有tagid
        taglist = self.get_tag_list().json().get('taglist')
        tagid_list = []
        for i in range(len(taglist)):
            tagid_list.append(taglist[i].get('tagid'))
        return tagid_list

    def tagname_is_in_lsit(self, tag):
        # 返回tagname是否在tagname_list
        tagname_list = self.get_tag_name_list()
        return tag in tagname_list

    def tagid_is_not_in_lsit(self, tag):
        # 返回tagid是否不在tagid_list
        tagid_list = self.get_tag_name_list()
        return tag not in tagid_list


