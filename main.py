import os

import numpy

import impont
import nuoyis_function
import nuoyis_webdriver

if __name__ == "__main__":
    if nuoyis_function.admin():
        # 设置窗口标题
        impont.os.system("title 诺依阁的工具箱 网站:https://blog.nuoyis.net Github地址:https://github.com/nuoyis/toolbox")
        impont.os.environ['PYTHONIOENCODING'] = 'GBK'
        a = b = c = 0

        # 主菜单样式
        while (1):
            print("---欢迎使用诺依阁工具箱---\n")
            impont.os.system('cls')
            gongleng = ["打开诺依阁的日记簿", "关于工作箱", "系统账号管理", "删除极域电子", "校园网登录", "动漫阅览", "网站工具", "Hexo专区", "按键专区", "退出工具箱"]
            gong = len(gongleng)
            lem = 1
            while lem <= gong:
                print(str(lem) + "." + gongleng[lem - 1])
                lem = lem + 1
            #print("---欢迎使用诺依阁工具箱---\n1.系统账号管理 2.删除极域电子 3.打开诺依阁的日记簿 4.关于工作箱 5.退出工具箱\n请注意:本软件仅供学习交流使用，任何违法违规行为自行承担")

            d = int(input("请输入1-"+str(lem-1)+"数字:"))

            if d == gong:
                exit()

            if d in numpy.arange(1, gong):
                if d == 1:
                    impont.os.system("start https://blog.nuoyis.net")
                elif d == 2:
                    print("此新版本为Python构建，原由C语言编写构建")
                    print("作者:诺依阁 新版编写时间:2023-09-30")
                    print("工具箱只是作者的学习内容，不为违法者任何行为买单")
                    print("@2020-2023 诺依阁 拥有除注释标识区域外拥有全部著作权和版权")
                    os.system("pause")
                elif d == 3:
                    nuoyis_function.systemuser()
                elif d == 4:
                    nuoyis_function.jiyukill()
                elif d == 5:
                    print("正在制作")
                elif d == 6:
                    nuoyis_function.acg()
                elif d == 7:
                    nuoyis_function.web()
                elif d == 8:

                elif d == 9:
            else:
                print("输入错误，请重新输入")
        impont.time.sleep(300)
    else:
        # 以管理员权限重新运行程序
        # impont.ctypes.windll.shell32.ShellExecuteW(None, "runas", impont.sys.executable, "", None, 1)
        impont.ctypes.windll.shell32.ShellExecuteW(None, "runas", impont.sys.executable, __file__, None, 1)

