"""
目标：完成数据库相关工具封装
分析：
    1、主要方法
        假设：def get_sql_one(sql)
    2、辅助方法
        获取对象连接
        获取游标对象
        关闭游标对象
        关闭连接对象
"""

#导包
import pymysql

# 新建工具类 数据库
class ReadDB:
    # 定义链接对象，类方法
    conn = None
    # 获取对象连接方法封装
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect("127.0.0.1",
                       "root",
                       "123456",
                       "hmtt",
                       charset = "utf-8")
            # 返回连接对象
            return self.conn
    # 获取游标对象方法封装
    def get_cursor(self):
        return self.get_conn().cursor()
    # 关闭游标对象方法封装
    def close_cursor(self,cursor):
        if cursor:
            cursor.close()
    # 关闭连接对象方法封装
    def close_conn(self):
        if self.conn:
            self.conn.close()
            #注意：关闭连接对象，对象还在内存中，需要手工设置为None
            self.conn = None


    #主要执行方法--》外界调用此方法就可以完成数据库相应的操作
    def get_sql_one(self):
        #定义游标对象及数据变量
        sursor = None
        data = None
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 获取执行方法
            sursor.execute(sql)
            # 获取结果
            data = sursor.fetchone()
        except Exception as e:
            print("数据库异常", e)
        finally:
            # 关闭游标对象
            self.close_cursor()
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data

    #获取所有数据库的结果集
    def get_sql_all(self,sql):
        # 定义游标对象及数据变量
        sursor = None
        data = None
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 获取执行方法
            sursor.execute(sql)
            # 获取结果
            data = sursor.fetchall()
        except Exception as e:
            print("数据库异常", e)
        finally:
            # 关闭游标对象
            self.close_cursor()
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data
    #修改，删除，新增
    def updata_sql(self,sql):
        # 定义游标对象及数据变量
        sursor = None
        data = None
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 获取执行方法
            sursor.execute(sql)
            #提交事务
            self.conn.commit()
        except Exception as e:
            #事务回滚
            self.conn.rollback()
            print("事务回滚", e)
        finally:
            # 关闭游标对象
            self.close_cursor()
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data

