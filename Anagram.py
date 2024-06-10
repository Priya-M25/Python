def char_count(w):
    count={}
    for i in w:
        if i in count:                             
            count[i]+=1
        else:
            count[i]=1
    return count

word="ate"
l=['care','hair','tea','eat']
rl=[]

for i in l:
    if char_count(i)==char_count(word):
        rl.append(i)
print(rl)

''' OUTPUT -
['tea', 'eat']
'''
