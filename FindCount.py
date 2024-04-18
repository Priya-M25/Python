def findCount(arr,l,num,diff):
    c=0
    for i in range(l):
        if abs(arr[i]-num)<=diff:
            c+=1
    return c

arr=[12,3,14,56,77,13]
num=13
diff=2
l=len(arr)
res=findCount(arr,l,num,diff)
print(res)
