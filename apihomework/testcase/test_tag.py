"""
用通讯录的增删改查，实现接口的api封装和测试用例编写
"""
from api.tag import TagApi


class TestTag:
    def setup_class(self):
        # 实例化TagApi()
        self.tag = TagApi()

    def test_get_tag_list(self):
        # 测试标签列表的获取
        r = self.tag.get_tag_list()
        assert r.json().get('errcode') == 0

    def test_create_tag(self):
        # 测试新建标签
        r = self.tag.create_tag()
        assert r.json().get('errcode') == 0

    def test_delete_tag(self, get_time_tag):
        # 测试删除标签
        r = self.tag.delete_tag(get_time_tag)
        assert r.json().get('errcode') == 0
        assert self.tag.tagid_is_not_in_lsit(get_time_tag)

    def test_update_tag(self, get_time_tag):
        # 测试更新标签
        r = self.tag.update_tag(get_time_tag)
        assert r.json().get('errcode') == 0
        assert self.tag.tagname_is_in_lsit(get_time_tag)
