animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot", "dog"]
first_dog_index = animals.index("dog")
print(f"Index of first 'dog'is at index: {first_dog_index}")

second_dog_index = animals.index("dog", first_dog_index + 1)
print(f"Index of second 'dog' is at index: {second_dog_index}")

third_dog_index = animals.index("dog", second_dog_index + 1)
print(f"Index of third 'dog' is at index: {third_dog_index}")