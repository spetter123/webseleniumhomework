import time

import requests
from api.base_api import BaseApi
from data.member_data import member_data


class MemberApi(BaseApi):

    def create_member(self, data=None):
        # 创建成员
        if data is None:
            data = member_data
        return requests.post(self._URL + f"/user/create?access_token={self.token}", json=data)

    def delete_member(self, data=None):
        # 删除成员
        if data is None:
            data = member_data
        self.create_member(data)
        return requests.get(self._URL + f"/user/delete?access_token={self.token}&userid={data.get('userid')}")

    def update_member(self, data=None, updata_info=None):
        # 更新成员信息
        if data is None:
            data = member_data
            self.create_member(data)
        data.update(updata_info)
        return requests.post(self._URL + f"/user/update?access_token={self.token}", json=data)

    def get_mamber(self, data=None):
        # 获取成员信息
        if data is None:
            data = member_data
            self.create_member(data)
        return requests.get(self._URL + f"/user/get?access_token={self.token}&userid={data.get('userid')}")
