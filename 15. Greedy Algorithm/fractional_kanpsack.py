items = [(20,100), (30,120), (10,60)]
items.sort(key=lambda x: x[1]/x[0], reverse=True)

value = 0
capacity = 50
for w, v in items:
    if capacity >= w:
        value += v
        capacity -= w
    else:
        value += (v/w) * capacity
        break

print(f"Total value obtained: {value}")



#______________________________________________________

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsack(items, capacity):
    # Sort items by value-to-weight ratio (highest first)
    items.sort(key=lambda item: item.ratio, reverse=True)

    total_value = 0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.ratio * capacity
            break  # Knapsack is full

    print(f"Total value obtained: {total_value}")

# Example usage
items = [Item(20, 100), Item(30, 120), Item(10, 60)]
knapsack(items, 50)
