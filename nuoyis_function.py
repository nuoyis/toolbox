import impont

def systemuser():
    # print("---欢迎使用诺依阁工具箱---\n1.系统账号添加 2.删除系统账户 3.修改系统账户密码 4.查看用户列表 5.退出此功能")
    gongleng = ["系统账号添加","删除系统账户","修改系统账户密码","查看用户列表","退出此功能"]
    lem = 1
    while lem <= len(gongleng):
        print(str(lem)+"."+gongleng[lem-1])
        lem = lem+1
    usernum = int(input("请输入序号:"))
    if usernum in numpy.arange(1, gongneng):
        if usernum == 1:
            systemuseradd()
        elif usernum == 2:
            systemuserdel()
        elif usernum == 3:
            systemuserchangepassword()
        elif usernum == 4:
            impont.os.system("net user")
            input("按 Enter 继续...")
        else:
            input("按 Enter 继续...")
    else:
        print("输入不正确，请重新输入")
def hexo_main():
    gongleng = ["系统账号添加", "删除系统账户", "修改系统账户密码", "查看用户列表", "退出此功能"]
    lem = 1
    while lem <= len(gongleng):
        print(str(lem) + "." + gongleng[lem - 1])
        lem = lem + 1
    usernum = int(input("请输入序号:"))
    if usernum in numpy.arange(1, gongneng):
        if usernum == 1:
            hexo_picture()
        elif usernum == 2:
            typecho2hexo()
        else:
            input("按 Enter 继续...")
    else:
        print("输入不正确，请重新输入")

def systemuseradd():
    # 系统账户创建
    sysuser = input("请输入用户名:")
    syspassword = input("请输入密码:")
    print("正在添加中,请稍后:")
    impont.os.system("net user "+sysuser+" "+syspassword+" /add")
    if int(input("是否给予管理员权限，1是 ,2否定：")):
        impont.os.system("net localgroup administrators "+sysuser+" /add")
        print("给予账户管理员权限成功")
    else:
        print("你未给予账户管理员权限")
    print("账户创建命令执行成功")
    input("按 Enter 继续...")

def systemuserdel():
    # 系统账户删除
    sysuser = input("请输入用户名:")
    print("正在删除中,请稍后:")
    impont.os.system("net user "+sysuser+" /delete")
    print("账户删除命令执行成功")
    input("按 Enter 继续...")

def systemuserchangepassword():
    # 系统账户密码修改
    sysuser = input("请输入用户名:")
    print("正在修改中,请稍后:")
    impont.os.system("net user " + sysuser + " *")
    print("账户修改命令执行成功")
    input("按 Enter 继续...")

def jiyukill():
    # 极域电子进程删除
    print("正在删除极域电子进程")
    impont.os.system("@echo off")
    impont.os.system("sc stop tdnetfilter")
    impont.os.system("sc stop tdfilefilter")
    impont.os.system("taskkill /im StudentMain.exe /f")
    impont.os.system("taskkill /im StudentEX.exe  /f")
    impont.os.system("taskkill /im MasterHelper.exe /f")
    print("删除进程完毕")
    input("按 Enter 继续...")

def web():
    #网站工具箱
    gongleng = ["本地ping", "网站测速", "页面截图下载", "打开网站"]
    lem = 1
    while lem <= len(gongleng):
        print(str(lem)+"."+gongleng[lem-1])
        lem = lem+1
    usernum = int(input("请输入序号:"))
    if usernum in [1, 2, 3]:
        if usernum == 2:
            print("该API由夏柔(https://api.aa1.cn)提供")
            url = "https://ml.v.api.aa1.cn/ping.php"
            params = {
                "host": "blog.nuoyis.net"
            }
            response = impont.requests.get(url, params=params)
            data = response.json()
            print(data["msg"])
            input(":")
            print("获取到访问时间为"+data["time"]+",测速用的IP为:"+data["ip"])
            input("按任意键继续:")
    else:
        print("没有想要的结果哦")



def admin():
    try:
        return impont.ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def acg():
    i = 1
    while i:
        print("正在尝试加载，请稍后...")
        # 使用Get的方式调用API接口，并将返回的值保存为response
        response = impont.requests.get('https://api.nuoyis.net/yu-api/acg/?type=json')
        # 使用request内置的json()函数将数据解析为列表形式
        print("状态值:"+response.json()['code'])  # 根据想要获取的数据，直接使用索引就行输出
        print("图片地址:"+response.json()['acgurl'])
        print("图片类型:"+response.json()['size'])
        print("图床均采用cloudflare进行缓存和防护")
        impont.os.system('start '+response.json()['acgurl'])
        if not input("是否接着观看，是回复1，否则任意键:") == "1":
            i = 0