'''
Problem statement :-
The problem is to write a program that takes an integer 'n' as input and prints the sum of all its even digits and the sum of all its odd digits separately.

Input:
132456

Output:
12 9

'''

# Function to calculate sum of even and odd digits
def sum_of_even_and_odd(n):
    sn = str(n)
    sum_e = sum_o = 0
    for i in range(len(sn)):
        if int(sn[i]) % 2 == 0:
            sum_e += int(sn[i])
        else:
            sum_o += int(sn[i])
    return sum_e, sum_o

# Input
n = int(input())

# Calculate sum of even and odd digits
even_sum, odd_sum = sum_of_even_and_odd(n)

# Output
print(even_sum, odd_sum)

