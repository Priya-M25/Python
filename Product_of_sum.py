n=int(input("Enter the value :- "))
print(f"Multiple of {n}:-")
sum=0
for i in range(1,11):
    x=i*n
    sum+=x
    
    print(x,end=' , ')
print(f"\nSum of Multiples of {n} is - ",sum)