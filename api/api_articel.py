# 导包
import requests

# 新建对象类
class ApiArticel(object):
    # 新建收藏文章的方法
    def api_post_collection(self,url,headers,data):
        #调用poet请求
        return requests.post(url,headers=headers, json = data)

    #新建取消收藏文章的方法
    #调用delete方法，并返回响应对象
    def api_delete_articel(self,url,headers):
        #调用poet请求
        return requests.delete(url,headers=headers)

