import numbers


bool_list = [False, True, False,]
any_true = any(bool_list)
print(f"Is there any True in the list? {any_true}")  # Output: True
all_true = all(bool_list)
print(f"Are all values True in the list? {all_true}")  # Output: False
string = "hellow"
characters = list(string)
print(f"list of characters: {characters}")  # Output: ['h', 'e', 'l', 'l', 'o', 'w']  

reversed_numbers = list(reversed(numbers))
print(f"Reversed list: {reversed_numbers}")  # Output: [4, 3, 2, 1, 0]

enumerated_numbers = list(enumerate(numbers))
print(f"Enumerated list: {enumerated_numbers}")  # Output: [(0, 4), (1, 2), (2, 9), (3, 1), (4, 5), (5, 6)]
