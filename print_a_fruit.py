fruits=["apple","banana","cherry","apple"]
print("original list:",fruits)
#add element
fruit=["apple","banana"]
fruit.append("orange")
print("original list:",fruit)
#remove element
fruit=["apple","banana"]
if "banana" in fruit:
    fruit.remove("banana")
    print("original list:",fruit)
    #access by index
fruits=["apple","banana"]
print("first fruit:",fruit[0])
#list comprehension
fruit=["apple", "orange"]
upper_fruit=[fruit.upper() for fruit in fruit]
print("Upper case fruits:", upper_fruit)
#for Lower case
fruit=["APPLE", "ORANGE"]
lower_fruit=[fruit.lower() for fruit in fruit]
print("lower case fruit:", lower_fruit)