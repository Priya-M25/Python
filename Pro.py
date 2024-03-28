#ar=[7,4,8,2,9]
ar=[3,4,5,6,8,9]
for i in range (len(ar)):
    if i==0:
        maxn=ar[i]
        c=1
    elif (ar[i]>maxn):
        c+=1
        max=ar[i]
print(c)
