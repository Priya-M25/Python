''' Output
Enter the string :- apple
enter the no. of shifts :- 1
 bqqmf
'''
s = input("Enter the string :- ")
n = len(s)
shift = int(input("enter the no. of shifts :- "))

if shift < n:
    ns=' '
    for i in range(n):
        if s[i]!=' ':
            shifted_char = chr(ord(s[i]) + shift)  # Calculate shifted character
            ns+=shifted_char
        else:
            ns+=' '

print(ns)
