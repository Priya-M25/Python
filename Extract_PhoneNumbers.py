def extract_phone_numbers(paragraph):
    phone_numbers = []
    n = len(paragraph)
    
    for i in range(n - 9):
        # Extract a substring of 10 characters
        candidate = paragraph[i:i + 10]
        
        # Check if all characters in the candidate are digits
        if candidate.isdigit():
            # Check surrounding characters for common phone number delimiters
            if (i == 0 or not paragraph[i-1].isdigit()) and (i + 10 == n or not paragraph[i + 10].isdigit()):
                phone_numbers.append(candidate)
    
    return phone_numbers

# Example usage
paragraph = """
    You can reach us at 1234567890 or at 0987654321. For international queries, 
    you can call +18001234567 or +442079460958. Alternatively, contact our office 
    at 123-456-7890 or (123) 456 7890. John Doe, age 30, was born on 19891231. 
    The event is on 2022-04-01 9911667755.
"""
phone_numbers = extract_phone_numbers(paragraph)
print(phone_numbers)


''' OUTPUT :-

['1234567890', '0987654321', '9911667755']

'''
