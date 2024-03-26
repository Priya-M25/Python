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