shapes = ["circle", "square", "triangle", "rectangle", "hexagon"]
shapes.append("octagon")
print(f"Shapes after append: {shapes}")

shapes.extend(["nonagon", "decagon"])
print(f"Shapes after extend: {shapes}")

shapes.insert(2, "pentagon")
print(f"Shapes after insert: {shapes}")

shapes.remove("triangle")
print(f"Shapes after remove: {shapes}")

popped_shape = shapes.pop()
print(f"Popped shape: {popped_shape}")
print(f"Shapes after pop: {shapes}")

index_of_square = shapes.index("square")
print(f"Index of 'square': {index_of_square}")

count_of_squares = shapes.count("square")
print(f"Count of 'square': {count_of_squares}")

shapes.clear()
print(f"Shapes after clear: {shapes}")

shapes = ["circle", "square", "triangle", "rectangle", "hexagon"]
shapes.sort()
print(f"Shapes after sort: {shapes}")

shapes.reverse()
print(f"Shapes after reverse: {shapes}")