def package(weight1,price1,weight2,price2):
    package1 = price1 / weight1
    package2 = price2 / weight2
    if package1 > package2:
        print("package2 has the better price")
    else:
        print("package1 has the better price")
def start():
    weight1,price1 = eval(input("Enter weight and price for package:"))
    weight2,price2 = eval(input("Enter weight and price for package:"))
    package(weight1,price1,weight2,price2)
start()