'''
目标：完成登录业务层实现
'''

#导包unittest ApiLogin
import unittest
# import api.api_login
from api.api_login import ApiLogin
from parameterized import  parameterized
from tools.read_json import ReadJson

#读取数据函数
def get_data():
    datas = ReadJson("login_more.json").read_json()
    # print(datas)
    arrs = []
    #使用遍历获取所有的value
    for datas in datas.values():
        arrs.append((datas.get("url"),
                     datas.get("mobile"),
                     datas.get("code"),
                     datas.get("expect_result"),
                     datas.get("status_code")))
    # print(arrs)
    return arrs


# 新建测试类
class TestLogin(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self, url,mobile,code,expect_result,status_code):
        s = ApiLogin().api_post_login(url, mobile, code)
        print(s.json())
        #  断言 响应信息 及 状态码
        self.assertEqual(expect_result, s.json()['message'])
        #断言响应状态码
        self.assertEqual(status_code, s.status_code)

if __name__ == '__main__':
    unittest.main()

"""
{'message': 'OK', 
 'data': {
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODA2NTQ5NjEsInVzZXJfaWQiOjEyMjMyMzYwMjI0OTAzNjU5NTIsInJlZnJlc2giOmZhbHNlfQ.hUT9L-YnD4wRCNn_q9GxxMgTDC2-IhaOY9kFz5t1fAQ', 
    'refresh_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODE4NTczNjEsInVzZXJfaWQiOjEyMjMyMzYwMjI0OTAzNjU5NTIsInJlZnJlc2giOnRydWV9.J4Fg3ggSNinqtdCd8AfuztzTFfOB9obPAzmHlsEALrE'
    }
}
有效期2个小时
"""