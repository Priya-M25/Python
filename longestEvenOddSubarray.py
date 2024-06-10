def longestEvenOddSubarray(arr, n):
    longest = 1
    cnt = 1
    for i in range(n - 1):
        if (arr[i] % 2 != arr[i + 1] % 2):  
            cnt += 1
        else:
            longest = max(longest, cnt)
            cnt = 1
    longest = max(longest, cnt)
    if longest > 1:
        return longest 
    else:
        return  0  

arr = [10,12,14, 7, 8]
n = len(arr)
print(longestEvenOddSubarray(arr, n)) 

# OUTPUT - 3 (As 14 7 8 )
