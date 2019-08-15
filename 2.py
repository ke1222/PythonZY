import math
radius,length = eval(input("Enter the radius and length of a cylinder:"))
area = radius * radius * math.pi
volume = area * length
print("The area is",' %.4f'%area)
print("The voiume is",' %.1f'%volume)
