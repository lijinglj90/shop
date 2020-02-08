"""
  目标：parameterized参数化组件
  安装：pip install parameterized
  使用：
    @parameterized.expand([("foo", 1, 2)])
    @parameterized.expand(参数)
    参数：
    单个参数格式：列表  如：[值1，值2]
    多个参数：列表嵌套元组  如[(参1值，参2值)]
"""
# 导包
import unittest
from parameterized import  parameterized

# 新建测试类
class TestPara(unittest.TestCase):
    @parameterized.expand([('admin','1234'),('001','4321')])
    def test_para(self, username,password):
        print('用户名：',username)
        print('密码：',password)
