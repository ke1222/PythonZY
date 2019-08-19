def numberOfDaysInAYear(year1,year2):
    for i in range(year1,year2):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            print(i,"年有366天,是闰年")
        else:
            print(i,"年有365天")
def start():
    year1 = 2010
    year2 = 2021
    numberOfDaysInAYear(year1,year2)
start()