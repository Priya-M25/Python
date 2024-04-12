'''Problem Statement:
You are given a sorted integer array 'arr' of size 'n'. Your task is to remove the duplicates from the array such that each element appears only once. Return the new array containing only unique elements.

Output :-
[1, 2, 3, 4, 5]
'''
def removeDuplicates(arr, n):
    sa = []
    for i in range(n):
        is_duplicate = False
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                is_duplicate = True
                break
        if not is_duplicate:
            sa.append(arr[i])
    return sa
# Example usage
arr = [1, 1, 2, 2, 3, 4, 4, 5]
n = len(arr)
unique_elements = removeDuplicates(arr, n)
print(unique_elements)
