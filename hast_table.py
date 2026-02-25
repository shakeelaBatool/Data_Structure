table= [None]*10
print(len(table))
name_1="Ali"
value=25
index=0
for i in name_1:
    index+=(ord(i))
index=index%10
table[index]=value

print(f'{name_1} is at index {index}: {table[index]}')
