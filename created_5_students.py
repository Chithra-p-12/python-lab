# 1. Create a list of 5 numbers and print all elements
numbers = [2, 4, 6, 8, 10]
print(numbers)

# 2. Print first and last element of a list
lst = [10, 20, 30, 40, 50]
print(lst[0], lst[-1])

# 3. Add number 100 to the list
lst2 = [1, 2, 3, 4]
lst2.append(100)
print(lst2)

# 4. Remove element 3 from the list
lst3 = [1, 2, 3, 4, 5]
lst3.remove(3)
print(lst3)

# 5. Find the sum of all elements
lst4 = [5, 10, 15, 20]
print(sum(lst4))

# 6. Find the maximum and minimum
lst5 = [8, 3, 9, 1, 6]
print(max(lst5), min(lst5))

# 7. Create a tuple of 4 elements and print it
tup = (1, 2, 3, 4)
print(tup)

# 8. Print second and third element of tuple
tup2 = (10, 20, 30, 40)
print(tup2[1], tup2[2])

# 9. Unpack tuple into variables
tup3 = (5, 10, 15)
a, b, c = tup3
print(a, b, c)
