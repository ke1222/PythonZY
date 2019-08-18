list1 = []

for i in range(1,8):
    for j in range(1,8):
        if i != j and sorted([i,j]) not in list1:
            list1.append([i,j])            
print(list1)