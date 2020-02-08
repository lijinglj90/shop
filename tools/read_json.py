#读取json首先要导入json包
import  json
#打开文件并获取文件流
# with open('../data/login.json','r',encoding='utf-8') as f:
#     #调用load方法加载文件流
#     data = json.load(f)
#     print('数据流：',data)
#解决方案封装
# def read_json():
#     with open('../data/login.json', 'r', encoding='utf-8') as f:
#         # 调用load方法加载文件流
#         data = json.load(f)
#         return data
#使用参数替换
class ReadJson(object):
    def __init__(self,filename):
        self.filepath = '../data/'+filename
    def read_json(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            # 调用load方法加载文件流
            data = json.load(f)
            return data

if __name__ == "__main__":
    # 登录测试数据调试
    # data = ReadJson("login.json").read_json()
    # # print(data)
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("mobile"),
    #              data.get("code"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)

    #获取用户频道列表调试
    # data = ReadJson("channel.json").read_json()
    # # print(data)
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("headers"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)

    #收藏文章 调试
    # data = ReadJson("article_add.json").read_json()
    # print(data)
    # arrs = []
        # arrs.append((data.get("url"),
        #              data.get("headers"),
        #              data.get("data"),
        #              data.get("expect_result"),
        #              data.get("status_code")))
        # print(arrs)

    #取消收藏文章 调试
    data = ReadJson("article_cancel.json").read_json()
    # print(data)
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("status_code")))
    print(arrs)

'''
问题1:未经过封装无法在别的模块内使用
解决2：进行封装
问题2：数据存储文件有多个
解决2：使用参数替换静态写死的文件
问题3：parameterized 预期格式为列表嵌套元组
解决3：读取字典内容，并添加到列表 如[(参1值，参2值)]
问题4：多个参数预期格式为列表元组【（url,mobile),(url,mobil),】
解决4：可以利用字典中values()方法读取所有的值
'''