num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare using if-elif-else
if (num1 >= num2) and (num1 >= num3):
    highest = num1
elif (num2 >= num1) and (num2 >= num3):
    highest = num2
else:
    highest = num3

print("The highest number is:", highest)