''' Problem Statement

You are given a binary string arr that consists of digits and certain operations represented by characters 'A', 'B', and 'C'. Each operation is performed on two consecutive digits in the string, 
with the result replacing the first digit. The operations are defined as follows:

'A': Perform a bitwise AND operation between the two digits.
'B': Perform a bitwise OR operation between the two digits.
'C': Perform a bitwise XOR operation between the two digits.
Your task is to implement a function operationBinaryString(arr) that calculates the result of applying these operations to the digits in the given order.

'''
def operationBinaryString(arr):
    result = None
    i = 0
    while i + 2 < len(arr):
        if arr[i].isdigit() and arr[i + 1] == 'A' and arr[i + 2].isdigit():
            if result is None:
                result = int(arr[i]) & int(arr[i + 2])
            else:
                result = result & int(arr[i + 2])
        elif arr[i].isdigit() and arr[i + 1] == 'B' and arr[i + 2].isdigit():
            if result is None:
                result = int(arr[i]) | int(arr[i + 2])
            else:
                result |=  int(arr[i + 2])  # Accumulate using bitwise OR
        elif arr[i].isdigit() and arr[i + 1] == 'C' and arr[i + 2].isdigit():
            if result is None:
                result = int(arr[i]) ^ int(arr[i + 2])
            else:
                result ^= int(arr[i + 2])  # Accumulate using bitwise XOR
        i += 2  # Move to the next group of three characters
    return result

arr = "1C0C1C1A0B1"
#arr="1A0B1A1C0A0"
#arr="0B1A0B1C0"
print(operationBinaryString(arr))  # Output: 1
