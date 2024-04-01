'''
Problem Statement:
The given code defines a function `Count(s)` that takes a string `s` as input. The function counts the occurrences of '*' and '#' characters in the string `s` and returns the difference between the counts of '*' 
and '#'.
If there are more '*' characters than '#', it returns the difference. If there are more '#' characters than '*', it returns the negative difference. If the counts are equal, it returns 0.

Output:
For the provided input string s = "###****", the output is 1.

'''

def Count(s):
    cs,ch=0,0
    for i in range(len(s)):
        if s[i]=='*':
            cs+=1
        elif s[i]=='#':
            ch+=1
    if cs>ch:
        r=cs-ch
    elif ch>cs:
        r=cs-ch
    else:
        r= 0
    return r
s="###****"
res=Count(s)
print(res)
