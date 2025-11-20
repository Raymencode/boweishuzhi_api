import sqlalchemy
import pymysql
from common.handle_conf import conf


"""
with 启动上下文管理器的关键字

上下文管理器协议 如果一个类中实现了如下两个方法，那么该类就实现了上下文管理协议，可以通过with进行操作
            __enter__:
            __exit__:
"""


class HandleDB:
    # 建立mysql连接
    # 方式一初始化时直接读取配置
    def __init__(self):
        self.con = pymysql.connect( host=conf.get("mysql", "host"),
                                            port=eval(conf.get("mysql", "port")),
                                            user=conf.get("mysql", "username"),
                                            password=conf.get("mysql", "password"),
                                            charset=conf.get("mysql", "charset"),
                                       # 设置游标对象返回的数据类型，默认是元组
                                            cursorclass=pymysql.cursors.DictCursor
                                       )
    # 方式二实例化时传入连接配置
    # def __init__(self, host, port, user, password,charset,  *args, **kwargs):
    #     self.con = pymysql.connect(host=host,
    #                                port=port,
    #                                user=user,
    #                                password=password,
    #                                charset=charset,
    #                                # 设置游标对象返回的数据类型，默认是元组
    #                                # cursorclass=pymysql.cursors.DictCursor
    #                                )

    def getone(self, sql):
        cur = self.con.cursor()
        with cur as cursor:
            cursor.execute(sql)
            self.con.commit()
            res = cursor.fetchone()
            # 关闭游标
            cursor.close()
            # self.con.close()
        return res

    def getall(self, sql):
        cur = self.con.cursor()
        with cur as cursor:
            cursor.execute(sql)
            self.con.commit()
            res = cursor.fetchall()
            # 关闭游标
            cursor.close()
        return res

    def count_num(self, sql):
        cur = self.con.cursor()
        with cur as cursor:
            cursor.execute(sql)
            self.con.commit()
            res = len(cursor.fetchall())
            cursor.close()
        return res

    def __del__(self):
        """
        关闭连接
        :return:
        """
        self.con.close()


db = HandleDB(host=conf.get("mysql", "host"),
              port=conf.getint("mysql", "port"),
              user=conf.get("mysql", "username"),
              password=conf.get("mysql", "password"),
              charset=conf.get("mysql", "charset"))



