sum_ = 0
for i in range(1,100000):
    sum_ += 4*((-1)**(i+1)/(2*i-1))
print(sum_)