#读取json首先要导入json包
import  json

class ReadJson(object):
    def __init__(self,filename):
        self.filepath = '../data/'+filename
    def read_json(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            # 调用load方法加载文件流
            data = json.load(f)
            return data

if __name__ == "__main__":
    datas = ReadJson("login_more.json").read_json()
    print(datas)
    arrs = []
    #使用遍历获取所有的value
    for datas in datas.values():
        arrs.append((datas.get("url"),
                     datas.get("mobile"),
                     datas.get("code"),
                     datas.get("expect_result"),
                     datas.get("status_code")))
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