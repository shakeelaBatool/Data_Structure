list_bu = [7, 12, 9, 11, 3]
n = len(list_bu)

for i in range(n):
    for j in range(n - 1):   # sirf n-1 tak
        if list_bu[j] > list_bu[j + 1]:
            list_bu[j], list_bu[j + 1] = list_bu[j + 1], list_bu[j]

print(list_bu)
