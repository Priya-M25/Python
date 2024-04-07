''' OUTPUT :-
Enter the String: apple
Enter the first character: p
Enter the second character: i
aiile
'''

def replaceCharacter(string, n, c1, c2):
    if string is None:
        return ""
    new_string = ""
    for i in range(n):
        if string[i] == c1:
            new_string += c2
        elif string[i] == c2:
            new_string += c1
        else:
            new_string += string[i]
    return new_string

s = input("Enter the String: ")
c1 = input("Enter the first character: ")
c2 = input("Enter the second character: ")
n = len(s)
res = replaceCharacter(s, n, c1, c2)
if res:
    print(res)
else:
    print("invalid")
