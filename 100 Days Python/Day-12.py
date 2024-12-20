"""



Hash Table:
A hash table is a data structure that stores key-value pairs. 
It uses a hash function to compute an index into an array of buckets, from which the desired value can be found. 
Python implements hash tables through dictionaries.

Hash Set:
A hash set is a collection of unique elements. 
It is implemented in Python using the set type, 
which also uses a hash table under the hood for quick lookups.

Hash Map:
A hash map is essentially the same as a hash table, 
focusing on the mapping from keys to values. 
In Python, dictionaries serve as hash maps.



"""

# code #
# Hash Table, Hash Set, and Hash Map example in Python

# Hash Table using Python dictionary
hash_table = {}  # Empty hash table
hash_table['name'] = 'Anas'
hash_table['age'] = 20
hash_table['city'] = 'Peshawar'

print("Hash Table:")
for key, value in hash_table.items():
    print(f"{key}: {value}")

# Hash Set using Python set
hash_set = set()  # Empty hash set
hash_set.add('Python')
hash_set.add('JavaScript')
hash_set.add('C++')
hash_set.add('Python')  # Duplicate won't be added

print("\nHash Set:")
print(hash_set)

# Hash Map as a Dictionary
hash_map = {
    '101': 'John Doe',
    '102': 'Jane Smith',
    '103': 'Alice Johnson'
}

# Access and modify hash map
print("\nHash Map:")
print("Original:", hash_map)
hash_map['104'] = 'Bob Brown'  # Adding new entry
del hash_map['102']            # Deleting an entry
print("Modified:", hash_map)

# Combine concepts: Using hash map and hash set together
print("\nCombine Hash Map and Hash Set:")
unique_values = set(hash_map.values())  # Extract unique values from hash map
print("Unique Values:", unique_values)

# Demonstrating key lookups in Hash Table and Hash Map
key = 'name'
if key in hash_table:
    print(f"\nKey '{key}' found in hash table with value: {hash_table[key]}")
else:
    print(f"\nKey '{key}' not found in hash table.")
