students = ["kaisamba", "foday", "sharon"]
print(students)

print(f"My best friend is {students[0]}")
print(f"My best friend is {students[1]}")
print(f"My best friend is {students[2]}")

# Get the length of the an item in a list

print(students.index("kaisamba"))
print(students.index("sharon"))

# Get the number of items in a list
print(f"The total items in the list is {len(students)}")

# add an item to the list
students.append("isatu")
print(students)
students+=["mohamed", "john", "Bintu"]

print(students)

# add another students to another index
students.insert(4, "Donald")
print(students)

#  extend a list or another list to the existing list
fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)
print(students)

# to remove an item from the list
fruits.remove("Mango")

students.pop()
students.pop()
thirditem = students.pop()
print(students)
print(thirditem)