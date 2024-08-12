# Create a dictionary with some initial key-value pairs
my_dictionary = {
    "apple": "A fruit that red, green, or yellow.",
    "banana": "A long, yellow fruit that is sweet and soft inside.",
    "cat": "A small, domesticated carnivorous mammal with soft fur.",
}

# 1. Print the entire dictionary
print("Original Dictionary:", my_dictionary)

# 2. Access and print a specific value using a key
print("Definition of 'apple':", my_dictionary["apple"])

# 3. Add a new key-value pair to the dictionary
my_dictionary["dog"] = "A domesticated carnivorous mammal with a barking sound."
print("After adding 'dog':", my_dictionary)

# 4. Update the value of an existing key
my_dictionary["apple"] = "A sweet fruit that comes in various colors."
print("After updating 'apple':", my_dictionary)

# 5. Remove a key-value pair from the dictionary
del my_dictionary["banana"]
print("After removing 'banana':", my_dictionary)

# 6. Check if a key exists in the dictionary
if "cat" in my_dictionary:
    print("The key 'cat' exists in the dictionary.")

# 7. Loop through the dictionary and print all key-value pairs
print("Looping through the dictionary:")
for key, value in my_dictionary.items():
    print(f"{key}: {value}")

# 8. Get the length of the dictionary
print("Length of the dictionary:", len(my_dictionary))

# 9. Get all keys from the dictionary
keys = my_dictionary.keys()
print("Keys in the dictionary:", keys)

# 10. Get all values from the dictionary
values = my_dictionary.values()
print("Values in the dictionary:", values)

# 11. Get all key-value pairs as a list of tuples
items = my_dictionary.items()
print("Key-value pairs in the dictionary:", items)

# 12. Use the `get()` method to access a value safely
apple_value = my_dictionary.get("apple", "Not found")
print("Value for 'apple' using get():", apple_value)

# 13. Use the `pop()` method to remove a key and return its value
cat_value = my_dictionary.pop("cat", "Not found")
print("Value for 'cat' after popping:", cat_value)
print("Dictionary after popping 'cat':", my_dictionary)

# 14. Clear all key-value pairs from the dictionary
my_dictionary.clear()
print("Dictionary after clearing all items:", my_dictionary)
