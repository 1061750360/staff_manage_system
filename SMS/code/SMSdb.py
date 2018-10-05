from pymysql import connect


class MysqlHelp:
    def __init__(self, database, host="localhost", user="root",
                 password="123456", charset="gbk", port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port

    def open(self):
        self.conn = connect(database=self.database,
                            host=self.host,
                            user=self.user,
                            password=self.password,
                            charset=self.charset,
                            port=self.port)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    # 数据库写入操作
    def workOn(self, sql, L=[]):
        self.open()
        try:
            self.cur.execute(sql, L)
            self.conn.commit()
            print("workOn OK")
            self.close()
            return 1     #   1代表执行成功
        except Exception as e:
            self.conn.rollback()
            print("workOn Failed", e)
            self.close()
            return e   #   e代表执行失败,返回该错误信息

    # 数据库读取操作
    def getAll(self, sql, L=[]):
        self.open()
        self.cur.execute(sql, L)
        result = self.cur.fetchall()
        self.close()
        return result

