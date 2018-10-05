from socket import *
from threading import *
import traceback
import sys
from SMSdb import MysqlHelp
import time
import datetime


IP_PORT = ("127.0.0.1",8888)
smsdb = MysqlHelp('sms')   #创建数据库操作对象
curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  #获取当前时间存入curtime中

#改方法用于查找数据库来判断是否允许成功登录
def do_login(msg):
    name = msg.split("#")[0][3:]
    password = msg.split("#")[-1]
    select_sql = "select password,powerlimit from user where username=%s;"
    result = smsdb.getAll(select_sql,[name])
    print(result)
    if len(result) == 0 or password != result[0][0]:
        return "login failed"
    elif password == result[0][0] and result[0][1] == 'admin':
        return 'admin login ok'
    elif password == result[0][0] and result[0][1] == 'user':
        return 'user login ok'

#处理添加员工信息的方法
def add_staff_info(msg):
    msg = msg[3:].split("#")
    select_sql = "select * from pinfo where pid=%s;"
    result = smsdb.getAll(select_sql,[msg[0]])
    if len(result) != 0:   #若result不为空，则表示数据库中有该员工，返回exists（存在）
        return "exists"
    else:
        insert_sql = "insert into pinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                     "%s,%s,%s,%s,%s,%s);"
        pcreatetime = curtime
        plastchangetime = curtime
        a = smsdb.workOn(insert_sql,[msg[0],msg[1],msg[2],msg[3],msg[4],msg[5],msg[6],msg[7],
                                     msg[8],msg[9],msg[10],msg[11],msg[12],pcreatetime,
                                     plastchangetime,msg[13],msg[14]])
        if a == 1:
            return "add ok"
        else:
            return str(a)

#处理删除员工信息的方法
def delete_staff_info(msg):
    pid = msg[3:]
    select_sql = "select * from pinfo where pid=%s;"
    result = smsdb.getAll(select_sql,[pid])
    if len(result) == 0:
        #若result为空，则表示数据库中没有该员工，
        # 返回not exists（不存在）,存在则执行删除操作
        return "not exists"
    else:
        delete_sql = "delete from pinfo where pid=%s;"
        a = smsdb.workOn(delete_sql,[pid])
        if a == 1:
            return "delete ok"
        else:
            return str(a)

#更新员工数据
def update_staff_info(msg):
    msg = msg[3:].split("#")
    pid = msg[0]
    select_sql = "select * from pinfo where pid=%s;"
    result = smsdb.getAll(select_sql,[pid])
    if len(result) == 0:   #若result为空，则表示数据库中没有该员工，返回not exists（不存在）,存在则执行更新操作
        return "not exists"
    else:
        update_sql = "update pinfo set pjid=%s, pdid=%s, pname=%s, pgender=%s, pbirth=%s, " \
                     "pindate=%s, pschoolage=%s, pphone=%s, paddress=%s,psalary=%s, phobby=%s, " \
                     "pdept=%s,plastchangetime=%s, status=%s, ppassword=%s where pid=%s;"
        a = smsdb.workOn(update_sql,[msg[1],msg[2],msg[3],msg[4],msg[5],msg[6],msg[7],msg[8],
                                     msg[9],msg[10],msg[11],msg[12],curtime,msg[13],msg[14],pid])
        if a == 1:
            return "update ok"
        else:
            return str(a)

#查询员工信息
def select_staff_info(msg):
    pid = msg[3:]
    select_sql = "select * from pinfo where pid=%s;"
    result = smsdb.getAll(select_sql,[pid])
    if len(result) == 0:   #若result为空，则表示数据库中没有该员工，返回not exists（不存在）,存在则执行删除操作
        return "not exists"
    else:
        L = []
        for i in result[0]:
            if type(i) is int:
                L.append(str(i))
            elif type(i) is datetime.datetime:
                L.append(i.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                L.append(i)
    data = "#".join(L)
    return data

#处理添加部门信息的方法
def add_dept_info(msg):
    msg = msg[3:].split("#")
    select_sql = "select * from dept where did=%s;"
    result = smsdb.getAll(select_sql,[msg[0]])
    if len(result) != 0:   #若result不为空，则表示数据库中有该部门，返回exists（存在）
        return "exists"
    else:
        insert_sql = "insert into dept values(%s,%s,%s,%s,%s);"
        createtime = curtime
        lastchangetime = curtime
        a = smsdb.workOn(insert_sql,[msg[0],msg[1],createtime,lastchangetime,msg[2]])
        if a == 1:
            return "add ok"
        else:
            return str(a)

#处理删除部门信息的方法
def delete_dept_info(msg):
    did = msg[3:]
    select_sql = "select * from dept where did=%s;"
    result = smsdb.getAll(select_sql,[did])
    if len(result) == 0:
        #若result为空，则表示数据库中没有该部门，
        # 返回not exists（不存在）,存在则执行删除操作
        return "not exists"
    else:
        delete_sql = "delete from dept where did=%s;"
        a = smsdb.workOn(delete_sql,[did])
        if a == 1:
            return "delete ok"
        else:
            return str(a)


#处理更新部门信息的方法
def update_dept_info(msg):
    msg = msg[3:].split("#")
    did = msg[0]
    select_sql = "select * from dept where did=%s;"
    result = smsdb.getAll(select_sql,[did])
    if len(result) == 0:
        #若result为空，则表示数据库中没有该部门，
        # 返回not exists（不存在）,存在则执行更新操作
        return "not exists"
    else:
        update_sql = "update pinfo set dname=%s, lastchangetime=%s,status=%s where did=%s;"
        a = smsdb.workOn(update_sql,[msg[1],curtime,msg[2],did])
        if a == 1:
            return "update ok"
        else:
            return str(a)


#处理查询部门信息的方法
def select_dept_info(msg):
    did = msg[3:]
    select_sql = "select * from dept where did=%s;"
    result = smsdb.getAll(select_sql,[did])
    if len(result) == 0:
        #若result为空，则表示数据库中没有该部门，
        # 返回not exists（不存在）,存在则执行删除操作
        return "not exists"
    else:
        L = []
        for i in result[0]:
            if type(i) is int:
                L.append(str(i))
            elif type(i) is datetime.datetime:
                L.append(i.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                L.append(i)
    data = "#".join(L)
    return data



#客户端处理函数
def handler(connfd):
    while True:
        try:
            msg = connfd.recv(1024).decode()
            if msg[:3] == "Ll$":
                result = do_login(msg)
                print("Connect from",connfd.getpeername(),":",msg)
                connfd.send(result.encode())
            elif msg[:3] == "As$":
                data = add_staff_info(msg)
                connfd.send(data.encode())
            elif msg[:3] == "Ds$":
                data = delete_staff_info(msg)
                connfd.send(data.encode())
            elif msg[:3] == "Us$":
                data = update_staff_info(msg)
                connfd.send(data.encode())
            elif msg[:3] == "Ss$":
                data = select_staff_info(msg)
                connfd.send(data.encode())
            elif msg[:3] == "Ad$":
                data = add_dept_info(msg)
                connfd.send(data.encode())
            elif msg[:3] == "Dd$":
                data = delete_dept_info(msg)
                connfd.send(data.encode())
            elif msg[:3] == "Ud$":
                data = update_dept_info(msg)
                connfd.send(data.encode())
            elif msg[:3] == "Sd$":
                data = select_dept_info(msg)
                connfd.send(data.encode())
            elif msg[:3] == "E$":
                connfd.close()
                break
        except ConnectionResetError:
            print(connfd.getpeername(),"客户端断开连接")
            connfd.close()
            break


#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(IP_PORT)
s.listen(5)
print("服务器已启动...")

#等待客户端请求
while True:
    try:
        connfd,addr = s.accept()
        print(connfd.getpeername(),"已连接")
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception:
        traceback.print_exc()
        continue

    t = Thread(target = handler,args = (connfd,),daemon=True)
    t.start()


