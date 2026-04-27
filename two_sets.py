# 1. Find union of two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_result = set_a.union(set_b)
print("Union of sets:", union_result)

# 2. Find intersection of two sets
intersection_result = set_a.intersection(set_b)
print("Intersection of sets:", intersection_result)

# 3. Remove duplicates from a list using a set
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print("List after removing duplicates:", unique_list)

# 4. Count frequency of characters using a dictionary
def count_char_frequency(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

text = "hello world"
char_count = count_char_frequency(text)
print("Character frequency:", char_count)

# 5. Create a dictionary and search for a key value
my_dict = {"name": "Alice", "age": 25,  "city": , "bangalore"}
