'''
Problem Statement:
The code is intended to calculate the power of two individuals, Stephan and Demon, based on a given list of numbers. 
The list represents the strengths of their minions. The code first sorts the list of strengths in ascending order and 
then distributes them to Stephan and Demon in a way that maximizes Stephan's power while minimizing Demon's power.

[0, 1, 2, 3, 5, 9]
Stephan power:  15
Demon power:  11

'''

l=[0,9,3,5,1,2]
#l=[8,9,1,7,6]
sum=0
for i in range(len(l)):
    sum+=l[i]
sl=sorted(l)
print(sl)
dp=sum
sp=0
i=len(sl)-1
while sp<dp:
    sp=sp+sl[i]
    dp=dp-sl[i]
    i-=1
print("Stephan power :- ",sp)
print("Demon power :- ",dp)
