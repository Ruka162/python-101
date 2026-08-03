def is_armstrong(number):
    # Convert the number to a string to easily iterate over digits
    str_num = str(number)
    num_digits = len(str_num)
    
    # Calculate the sum of each digit raised to the power of num_digits
    total = sum(int(digit) ** num_digits for digit in str_num)
    
    # Check if the total is equal to the original number
    return total == number

print(is_armstrong(153))  # Output: True
print(is_armstrong(123))  # Output: False
print(is_armstrong(9474))  # Output: True