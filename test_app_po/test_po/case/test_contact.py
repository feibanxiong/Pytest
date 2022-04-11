from faker import Faker

from test_app_po.test_po.page.app import App


class TestContact:
    def setup_class(self):
        # 设置mock数据，假名，（'zh_CN'）设置中国地区假名
        self.fake = Faker('zh_CN')

    def setup(self):
        # driver的初始化，app启动
        self.app = App()
        self.main = self.app.start()

    def teardowm(self):
        self.app.stop()
        # driver的关闭，driver销毁
        pass

    def test_addcontact(self):
        # mock一个假名
        name = self.fake.name()
        # mock一个假的手机号
        phone_num = self.fake.phone_number()
        result = self.main.goto_main().goto_addresslist().goto_addmember(). \
            click_addmember_menual().edit_member(name, phone_num).get_tip()

        assert result == "添加成功"
