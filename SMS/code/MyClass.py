from SMSdb import MysqlHelp
import time


smsdb = MysqlHelp('sms')   #创建数据库操作对象


#员工信息类
class Pinfo:
    def __init__(self,pid,pjid,pdid,pname,pgender,pbirth,pindate,pschoolage,pphone,paddress,
                        psalary,phobby,pdept,status,ppassword):
        self.pid = pid
        self.pjid = pjid
        self.pdid = pdid
        self.pname = pname
        self.pgender = pgender
        self.pbirth = pbirth
        self.pindate = pindate
        self.pschoolage = pschoolage
        self.pphone = pphone
        self.paddress = paddress
        self.psalary = psalary
        self.phobby = phobby
        self.pdept = pdept
        self.pcreatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.plastchangetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.status = status
        self.ppassword = ppassword

    def select_pinfo(self):
        select_sql = "select * from pinfo where pid=%s;"
        result = smsdb.getAll(select_sql,self.pid)
        return result

    def add_pinfo(self):
        select_sql = "insert into pinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        a = smsdb.workOn(select_sql,[self.pid,self.pjid,self.pdid,str(self.pname),str(self.pgender),self.pbirth,self.pindate,
                                 str(self.pschoolage),self.pphone,str(self.paddress),self.psalary,str(self.phobby),str(self.pdept),
                                 self.pcreatetime,self.plastchangetime,self.status,self.ppassword])
        return a
