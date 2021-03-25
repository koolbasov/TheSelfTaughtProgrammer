lst1 = [8, 19, 148, 4]
lst2 = [9, 1, 33, 83]

lst3 = []

for i in lst1:
    for j in lst2:
        print(i, "*", j)
        lst3.append(i*j)
        print(lst3)
        
