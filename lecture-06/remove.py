fruits_with_duplicates = ["apple", "banana", "cherry", "apple", "apple", "kiwi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Fruits after removing all 'apple': {fruits_with_duplicates}")  # Output: ['banana', 'cherry', 'banana', 'kiwi']
#ทำให้มีapple