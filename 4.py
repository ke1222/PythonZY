M = eval(input("Enter the amount of water in kilograms:"))
I = eval(input("Enter the initial temperature:"))
F = eval(input("Enter the final temperature:"))
Q = M * (F - I) * 4184
print("The energy needed is",Q)