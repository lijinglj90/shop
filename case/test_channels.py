'''
目标：完成登录业务层实现
'''

#导包unittest ApiChannels
import unittest
from api.api_channels import ApiChannels
from parameterized import  parameterized
from tools.read_json import ReadJson

#读取数据函数
def get_data():
    data = ReadJson("channel.json").read_json()
    # print(data)
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expect_result"),
                 data.get("status_code")))
    # print(arrs)
    return arrs


# 新建测试类-继承
class TestChannels(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_channels(self,url,headers,expect_result,status_code):
        # 暂时存放数据url headers
        # url = "http://ttapi.research.itcast.cn/app/v1_0/user/channels"
        # 提示token之前有Bearer和空格
        # headers = {"Content-Type":"application/json",
        #            "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODA2NTQ5NjEsInVzZXJfaWQiOjEyMjMyMzYwMjI0OTAzNjU5NTIsInJlZnJlc2giOmZhbHNlfQ.hUT9L-YnD4wRCNn_q9GxxMgTDC2-IhaOY9kFz5t1fAQ"}
        #  优化-调用登录方法
        s = ApiChannels().api_get_channels(url, headers)
        print(s.json())
        #  断言 响应信息 及 状态码
        #断言响应状态码
        # self.assertEqual(200, s.status_code)
        self.assertEqual(status_code, s.status_code)
        #  断言 响应信息 及 状态码
        self.assertEqual(expect_result, s.json()['message'])
        # self.assertEqual("OK", s.json()['message'])

if __name__ == '__main__':
    unittest.main()

