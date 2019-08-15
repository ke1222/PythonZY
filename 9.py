import random
emile = '123456@qq.com'
password = '123456'
for i in range(4):
    emile1 = input("请输入账号")
    password1 = input("请输入密码")
    if emile1 == emile and password1 == password:
        print("登录成功")
        break
    else:
        print("账号或密码错误")
        for j in range(3):
            yzm = random.randint(1000,9999)
            print(yzm)
            num = int(input("请输入验证码"))
            if num == yzm:
                print("验证码正确")
                break
            else:
                print("验证码不正确")
                num = input("请重新输入验证码")
    if i == 3:
        print("账号已被锁定")