def main():
    year = int(input('输入哪一年:'))
    m = int(input('输入月份1-12:'))
    d = int(input('输入月份第几天1-31:'))
    a = ['周六','周日','周一','周二','周三','周四','周五']
    if m == 1:
        m = 13
        year = year - 1
    if m ==2:
        m = 14
        year = year - 1
    h = int(d+((26*(m+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
    day = a[h]
    print('那一天是一周中的:%s' %day)
def Start():
    main()
Start()