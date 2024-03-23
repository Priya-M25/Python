''Problem Statement:
Write a function `rat_con(r, unit, n, arr)` that accepts four parameters:

1. `r`: a positive integer representing the number of rats present in an area,
2. `unit`: a positive integer representing the amount of food each rat consumes,
3. `n`: a positive integer representing the number of houses,
4. `arr`: a positive integer array of size `n`, where each ith element of `arr` represents the amount of food present in the (i+1)th house number (0 <= i < n).

The function should return an integer denoting the house number from which the rats can get enough food to satisfy their hunger. If the array is null, the function should 
return -1. If the total amount of food from all houses is not sufficient for all the rats, the function should return 0.
'''

def rat_con(r, unit, n, arr):
    if not arr:  # Check if the array is empty
        return -1
    else:
        total_food = 0
        for i in range(len(arr)):
            total_food += arr[i]
            if total_food >= r * unit:
                x = i + 1
                if x <= n:
                    return x
                else:
                    return 0
        return 0  # Return 0 if no valid number of houses found

r = 7
unit = 2
n = 8  # no. of houses
arr = [2, 8, 3, 5, 7, 4, 1, 2]

res = rat_con(r, unit, n, arr)

if res == -1:
    print("null array")
elif res == 0:
    print("insufficient food")
else:
    print("number of houses - ", res)


''' Output :-
number of houses -  4
'''
