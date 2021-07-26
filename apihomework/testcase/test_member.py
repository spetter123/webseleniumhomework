import time

import requests
from data.member_data import member_data
from api.member import MemberApi


class TestMember:
    def setup_class(self):
        self.Api = MemberApi()

    def test_create_member(self):
        # 测试创建成员接口
        r = self.Api.create_member()
        assert r.json().get('errcode') == 0

    def test_delete_member(self):
        # 测试删除成员接口
        data = member_data
        r = self.Api.delete_member(data)
        assert r.json().get('errcode') == 0
        assert self.Api.get_mamber(data).json().get('errcode') == 60111

    def test_update_member(self):
        # 测试更新成员信息接口
        data = member_data
        updata_info = {'name': "name" + str(int(time.time()))}
        r = self.Api.update_member(updata_info=updata_info)
        assert r.json().get('errcode') == 0
        assert self.Api.get_mamber(data).json().get('name') == updata_info.get('name')

    def test_get_member(self):
        # 测试获取成员接口
        r = self.Api.get_mamber()
        assert r.json().get('errcode') == 0

    # def test_delete_demo(self):
    #     # 删除指定id成员
    #     r = requests.get(
    #         f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.Api.token}&userid=zhangsan1627226880")
    #     return r.json()
