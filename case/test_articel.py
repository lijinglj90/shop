'''
目标：完成登录业务层实现
'''

#导包unittest ApiChannels
import unittest
from api.api_articel import ApiArticel
from parameterized import  parameterized
from tools.read_json import ReadJson

# 读取数据函数
def get_data_add():
    data = ReadJson("article_add.json").read_json()
    # print(data)
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")))
    # print(arrs)
    return arrs

# 获取取消收藏文件
def get_data_cancel():
    data = ReadJson("article_cancel.json").read_json()
    # print(data)
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("status_code")))
    # print(arrs)
    return arrs

# 新建测试类-继承
class TestChannels(unittest.TestCase):
    # 新建测试收藏方法
    @parameterized.expand(get_data_add())
    def test_login(self,url,headers,data,expect_result,status_code):
    # def test01_collection(self):
        # 暂时存放数据url headers  data
        # url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections"
        # 提示token之前有Bearer和空格
        # headers = {"Content-Type":"application/json",
    #         #            "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODA2NTQ5NjEsInVzZXJfaWQiOjEyMjMyMzYwMjI0OTAzNjU5NTIsInJlZnJlc2giOmZhbHNlfQ.hUT9L-YnD4wRCNn_q9GxxMgTDC2-IhaOY9kFz5t1fAQ"}
    #         # data = {"target": 1}
        #调用收藏文章方法
        s = ApiArticel().api_post_collection(url, headers, data)
        #查看响应数据结构--仅调试
        print('显示收藏成功返回结果',s.json())
        #  断言 响应信息 及 状态码        #  断言 响应信息
        self.assertEqual(expect_result, s.json()['message'])
        # self.assertEqual("OK", s.json()['message'])
        #断言响应状态码
        # self.assertEqual(201, s.status_code)
        self.assertEqual(status_code, s.status_code)


    #新建取消收藏文章方法
    @parameterized.expand(get_data_cancel())
    def test02_cancel(self,url,headers,status_code):
    # def test02_cancel(self):
        # 暂时存放数据url headers
        # url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections/1"
        # 提示token之前有Bearer和空格
        # headers = {"Content-Type": "application/x-www-form-urlencoded",
        #            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODA2NTQ5NjEsInVzZXJfaWQiOjEyMjMyMzYwMjI0OTAzNjU5NTIsInJlZnJlc2giOmZhbHNlfQ.hUT9L-YnD4wRCNn_q9GxxMgTDC2-IhaOY9kFz5t1fAQ"}
        s = ApiArticel().api_delete_articel(url, headers)
        print(s)
        # 断言响应状态码
        # self.assertEqual(204, s.status_code)
        self.assertEqual(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()

