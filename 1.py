a# Sample dictionary
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

# clear() - removes all items
my_dict.clear()
print("Dictionary after clear():", my_dict)

# Re-populating the dictionary
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

# items() - creates a tuple pair
print("Items of the dictionary as tuples:", my_dict.items())

# popitem() - pops one item
popped_item = my_dict.popitem()
print("Popped item:", popped_item)
print("Dictionary after popitem():", my_dict)

# keys() - list of keys
print("Keys of the dictionary:", my_dict.keys())

# values() - list of values
print("Values of the dictionary:", my_dict.values())
