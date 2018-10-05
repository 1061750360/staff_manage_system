from socket import *
import re


IP_PORT = ('127.0.0.1',8888)
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.connect(IP_PORT)



#添加员工信息
def add_staff_info():
    try:
        while True:
            pid = int(input("请输入员工ID:"))
            if not pid:
                break
            pjid = input("请输入职位ID")
            pdid = input("请输入部门ID:")
            pname = input("请输入员工姓名:")
            pgender = input("请输入员工性别:")
            pbirth = input("请输入员工出生日期:")
            pindate = input("请输入员工入职日期:")
            pschoolage = input("请输入员工学历:")
            pphone = int(input("请输入员工联系方式:"))
            paddress = input("请输入员工住址:")
            psalary = int(input("请输入员工薪金:"))
            phobby = input("请输入员工爱好:")
            pdept = input("请输入员工部门名称:")
            status = int(input("请输入员工状态:"))
            ppassword = input("请输入员工密码")
            tup = (str(pid),pjid,pdid,pname,pgender,pbirth,
                   pindate,pschoolage,str(pphone),paddress,
                    str(psalary),phobby,pdept,str(status),ppassword)
            L = (str(pid),pjid,pdid,pname,pgender,pschoolage,str(pphone),paddress,
                    str(psalary),phobby,pdept,str(status),ppassword)
            for i in L:
                if re.findall(r"\W",i):
                    print(i,"中包含特殊字符,请重新输入")
                    continue
            tup = "As$" + "#".join(tup)
            sockfd.send(tup.encode())
            msg = sockfd.recv(1024).decode()
            if msg == "exists":
                print("该员工ID已存在，请重新输入")
            elif msg == "add ok":
                print("添加信息成功")
                break
            else:
                print("添加失败,",msg)
    except ValueError:
        print("输入错误")


#删除员工信息
def del_staff_info():
    while True:
        try:
            pid = int(input("请输入要删除员工的员工ID:"))
            if not pid:
                break
            pid = "Ds$" + str(pid)
            sockfd.send(pid.encode())
            msg = sockfd.recv(1024).decode()
            if msg == "not exists":
                print("该员工ID不存在，请重新输入")
            elif msg == "delete ok":
                print("删除信息成功")
                break
            else:
                print("删除失败,", msg)
        except ValueError:
            print("输入错误")


#更新员工信息
def update_staff_info():
    while True:
        try:
            pid = int(input("请输入要修改的员工的员工ID:"))
            if not pid:
                break
            pjid = input("请输入更新后的职位ID")
            pdid = input("请输入更新后的部门ID:")
            pname = input("请输入更新后的员工姓名:")
            pgender = input("请输入更新后的员工性别:")
            pbirth = input("请输入更新后的员工出生日期:")
            pindate = input("请输入更新后的员工入职日期:")
            pschoolage = input("请输入更新后的员工学历:")
            pphone = int(input("请输入更新后的员工联系方式:"))
            paddress = input("请输入更新后的员工住址:")
            psalary = int(input("请输入更新后的员工薪金:"))
            phobby = input("请输入更新后的员工爱好:")
            pdept = input("请输入更新后的员工部门名称:")
            status = int(input("请输入更新后的员工状态:"))
            ppassword = input("请输入更新后的员工密码")
            tup = (str(pid), pjid, pdid, pname, pgender, pbirth, pindate, pschoolage,
                   str(pphone), paddress,str(psalary), phobby, pdept, str(status), ppassword)
            L = (str(pid), pjid, pdid, pname, pgender, pschoolage, str(pphone), paddress,
                 str(psalary), phobby, pdept, str(status), ppassword)
            for i in L:
                if re.findall(r"\W", i):
                    print(i, "中包含特殊字符,请重新输入")
                    continue
            tup = "Us$" + "#".join(tup)
            sockfd.send(tup.encode())
            msg = sockfd.recv(1024).decode()
            if msg == "not exists":
                print("该员工ID不存在，请重新输入")
            elif msg == "update ok":
                print("更新信息成功")
                break
            else:
                print("更新失败,", msg)
        except ValueError:
            print("输入错误")

#查询员工信息
def select_staff_info():
    while True:
        try:
            pid = int(input("请输入要查询员工的员工ID:"))
            if not pid:
                break
            pid = "Ss$" + str(pid)
            sockfd.send(pid.encode())
            msg = sockfd.recv(1024).decode()
            if msg == "not exists":
                print("该员工ID不存在，请重新输入")
            else:
                print("查询成功")
                msg = msg.split("#")
                print("员工ID", msg[0])
                print("职位ID", msg[1])
                print("部门ID", msg[2])
                print("员工姓名", msg[3])
                print("员工性别", msg[4])
                print("员工出生日期", msg[5])
                print("员工入职日期", msg[6])
                print("员工学历", msg[7])
                print("员工联系方式", msg[8])
                print("员工住址", msg[9])
                print("员工薪金", msg[10])
                print("员工爱好", msg[11])
                print("员工部门名称", msg[12])
                print("员工创建时间", msg[13])
                print("员工最后修改时间", msg[14])
                print("状态", msg[15])
                print("员工密码", msg[16])
                break
        except ValueError:
            print("输入错误")

#添加部门信息
def add_dept_info():
    try:
        while True:
            did = input("请输入部门编号:")
            if not did:
                break
            dname = input("请输入部门名称")
            status = int(input("请输入记录状态:"))
            tup = (did,dname,str(status))
            tup = "Ad$" + "#".join(tup)
            sockfd.send(tup.encode())
            msg = sockfd.recv(1024).decode()
            if msg == "exists":
                print("该部门已存在，请重新输入")
            elif msg == "add ok":
                print("添加信息成功")
                break
            else:
                print("添加失败,",msg)
    except ValueError:
        print("输入错误")


#删除部门信息
def del_dept_info():
    while True:
        try:
            did = input("请输入要删除的部门ID:")
            if not did:
                break
            did = "Dd$" + did
            sockfd.send(did.encode())
            msg = sockfd.recv(1024).decode()
            if msg == "not exists":
                print("该部门ID不存在，请重新输入")
            elif msg == "delete ok":
                print("删除信息成功")
                break
            else:
                print("删除失败,", msg)
        except ValueError:
            print("输入错误")


#更新部门信息
def update_dept_info():
    while True:
        try:
            did = input("请输入要更新信息的部门ID:")
            if not did:
                break
            dname = input("请输入部门名称")
            status = int(input("请输入记录状态:"))
            tup = (str(did), dname, status)
            tup = "Ud$" + "#".join(tup)
            sockfd.send(tup.encode())
            msg = sockfd.recv(1024).decode()
            if msg == "not exists":
                print("该部门ID不存在，请重新输入")
            elif msg == "update ok":
                print("更新信息成功")
                break
            else:
                print("更新失败,", msg)
        except ValueError:
            print("输入错误")

#查询部门信息
def select_dept_info():
    while True:
        try:
            did = input("请输入要查询部门的ID:")
            if not did:
                break
            did = "Sd$" + did
            sockfd.send(did.encode())
            msg = sockfd.recv(1024).decode()
            if msg == "not exists":
                print("该部门ID不存在，请重新输入")
            else:
                print("查询成功")
                msg = msg.split("#")
                print("部门ID", msg[0])
                print("部门名称", msg[1])
                print("记录创建时间", msg[2])
                print("最后修改时间", msg[3])
                print("记录状态", msg[4])
                break
        except ValueError:
            print("输入错误")



#员工信息管理界面
def staff_management():
    while True:
        print("-----------员工信息管理界面---------------")
        print("1.添加员工信息")
        print("2.删除员工信息")
        print("3.更新员工信息")
        print("4.查询员工信息")
        print("5.返回上一层")
        try:
            opt = int(input("请输入你要执行的操作:"))
        except ValueError:
            print("输入错误,请重新输入")
            continue
        if opt == 1:
            add_staff_info()
        elif opt == 2:
            del_staff_info()
        elif opt == 3:
            update_staff_info()
        elif opt == 4:
            select_staff_info()
        elif opt ==5:
            print("退出员工信息管理界面")
            break
        else:
            print("输入错误")


#部门信息管理界面
def dept_management():
    while True:
        print("-----------部门信息管理界面---------------")
        print("1.添加部门信息")
        print("2.删除部门信息")
        print("3.更新部门信息")
        print("4.查询部门信息")
        print("5.返回上一层")
        try:
            opt = int(input("请输入你要执行的操作:"))
        except ValueError:
            print("输入错误,请重新输入")
            continue
        if opt == 1:
            add_dept_info()
            continue
        elif opt == 2:
            del_dept_info()
        elif opt == 3:
            update_dept_info()
        elif opt == 4:
            select_dept_info()
        elif opt ==5:
            print("退出部门信息管理界面")
            break
        else:
            print("输入错误")

#公司基本信息管理
def company_basic_information_management():
    while True:
        print("-----------公司基本信息管理界面---------------")
        print("1.员工管理")
        print("2.部门管理")
        print("3.职位管理")
        print("4.用户管理")
        print("5.返回上一层")
        try:
            opt = int(input("请输入你要执行的操作:"))
        except ValueError:
            print("输入错误,请重新输入")
            continue
        if opt == 1:
            staff_management()
        elif opt == 2:
            dept_management()
        elif opt == 3:
            pass
        elif opt == 4:
            pass
        elif opt ==5:
            print("返回管理员界面")
            break
        else:
            print("输入错误")




#管理员可以操作的界面
def admin_window():
    while True:
        print("---------------管理员界面---------------")
        print("1.公司基本信息管理")
        print("2.请假与考勤管理")
        print("3.公告管理")
        print("4.留言管理")
        print("5.回收站")
        print("6.注销")
        print("-----------------------------------------")
        try:
            opt = int(input("请输入你要执行的操作:"))
        except ValueError:
            print("输入错误,请重新输入")
            continue
        if opt == 1:
            company_basic_information_management()
            continue
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            pass
        elif opt == 5:
            pass
        elif opt ==6:
            print("退出管理员界面")
            break
        else:
            print("输入错误")

#登录模块
def do_login():
    while True:
        name = input("请输入用户名:").strip()
        if name == "":
            print("用户名为空")
            continue
        password = input("请输入密码:").strip()
        if password == "":
            print("密码为空")
            continue
        msg = "Ll$"+name + "#" + password
        return msg


#主函数
def main():
    msg = do_login()
    #判断用户名和密码是否可以登录，若不可以，则一直循环，否则进入下一个逻辑代码
    while True:
        sockfd.send(msg.encode())
        data = sockfd.recv(1024).decode()
        print(data)
        if data == 'admin login ok':  #若管理员登录成功，则跳转到管理员登录界面
            admin_window()
            continue
        if data == 'user login ok':   #若普通用户登录成功，则跳转到普通用户登录界面
            print("普通用户界面。。。正在维修")
    sockfd.close()


if __name__ == '__main__':
    main()
