#set (mutable,unordered,no duplicate)
numbers={1,2,3,2,1}
print("set:",numbers)
#add numbers
numbers={1,2,3,5}
numbers.add(4)
print("set:",numbers)
#discard elements
numbers={2,5,3,2}
numbers.discard(2)
print("set:",numbers)

print("update set:",numbers)
#set operations
evens={2,4,6}
print("union:",numbers|evens)
print("intersection:",numbers&evens)