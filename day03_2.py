
feiyong = 10000
sum_ = 0
for i in range(1,14):
    feiyong *= 1.05
    if i == 10:
        print("十年之后的学费为:",'%.2f'%feiyong)
    if i > 9:
        sum_ += feiyong 
print("十年后大学四年的总学费为:",'%.2f'%sum_)
