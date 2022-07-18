a = [1, 2, 3 , 4]
b = [1, 2]

for i in b:
    for j in a:
        if (i == j):
            a.remove(j)

print(a)