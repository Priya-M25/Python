'''
Problem Statement:
The code aims to count the number of carries that occur when adding two numbers digit by digit. It iterates through the digits of the two numbers, calculates the sum along with any carry from the previous addition,
and counts the number of carries that occur.

OUTPUT :-
enter num1 :-982
enter num2 :-97
2

'''

def countCarry(n1,n2):
    carry,count=0,0
    while n1>0 or n2>0:
        d1=n1%10
        d2=n2%10
        sum=d1+d2+carry
        carry=sum//10
        if carry >0:
            count+=1
        n1/=10
        n2/=10
    return count
n1=int(input("enter num1 :-"))
n2=int(input("enter num2 :-"))
res=countCarry(n1,n2)
print(res)
