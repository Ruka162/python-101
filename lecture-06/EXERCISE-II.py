inventory = [
    ["apple", 50, 0.75],
    ["banana", 100, 0.50],
    ["orange", 75, 0.80],
]


def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity_sold
            return
    print(f"Item '{item_name}' not found in inventory.")
  
def calculate_total_value(inventory):
    total_value = 0
    for name, quantity, price in inventory:
        total_value += quantity * price
    return total_value

def find_most_valuable_item(inventory):
    most_expensive = max(inventory, key=lambda item: item[2])
    return most_expensive[0]


def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return
    inventory.append([item_name, quantity, price])
        
    
    
update_inventory(inventory, "banana", 20)
total_value = calculate_total_value(inventory)
print(f"Total value: {total_value}")

print("Most expensive item:", find_most_valuable_item(inventory))

add_item(inventory, "Eggs", 30, 0.25)
print(inventory)