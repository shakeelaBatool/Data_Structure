arr= [7,12,8,9,3]
n =len(arr)
#
for i in range (n):
        for j in range(i+1,n):
            
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            
print(arr)

