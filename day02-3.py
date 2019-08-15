def day():
    day1 = int(input('Enter today is day（周日为0，周一为1...周六为6):'))
    day2 = int(input('Enter the number of days elapsed since today:'))
    Today = oneday(day1)
    After = twoday(day1,day2)
    print("Today is",Today,"and the future day is",After)
def oneday(After):
    if After == 0:
        today = 'Sunday'
    elif After == 1:
        today = 'Monday'
    elif After == 2:
        today = 'Tuesday'
    elif After == 3:
        today = 'Wednesday'
    elif After == 4:
        today = 'Thursday'
    elif After == 5:
        today = 'Friday'
    elif After == 6:
        today = 'Saturday' 
    return today
def twoday(Today,After):
    After = (Today + After) % 7
    return oneday(After)
day()