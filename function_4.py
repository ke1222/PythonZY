def futureInvestmentValue(investmentAmount,yearlyInterestRate):
    month = (float(yearlyInterestRate))/12/100
    print("year",'\t',"Future Value")
    for years in range(1,31):
        futurevalue = investmentAmount*((1+month)**(12*years)) 
        print(years,'\t','%.2f'%futurevalue)
def start():
    investmentAmount = int(input("The amount invested:"))
    yearlyInterestRate = int(input("Annual interest rate:"))
    futureInvestmentValue(investmentAmount,yearlyInterestRate)
start()
