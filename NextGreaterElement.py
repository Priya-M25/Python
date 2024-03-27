'''
Question:

Given an array `arr`, find the next greater element for each element in the array. If there is no greater element to the right, then replace it with -1.

 output -> [6,8,8,8,-1,5,-1]
'''

l = []
arr = [4, 6, 3, 2, 8, 1, 5]
for i in range(len(arr)):
    found_greater = False
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            l.append(arr[j])
            found_greater = True
            break
    if not found_greater:
        l.append(-1)

print(l)  # Output: [6, 8, 8, 8, -1, 5, -1]