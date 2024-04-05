s = 'amrtrma'
i = 0
j = len(s) - 1
is_pali = True

while i <= j:
    if s[i] != s[j]:
        is_pali = False
        break
    i += 1
    j -= 1

if is_pali:
    print("true")
else:
    print("false")
