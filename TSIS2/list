# LIST items are ordered, changeable, allow duplicate
from builtins import print

thisList = ["apple", "banana", "cherry", "apple"];
print(thisList)
print(len(thisList))
# List items can be any data type
list1 = ["apple", "banana", "cherry"];
list2 = [1, 2, 3, 4, 5];
list3 = [True, False];
listCombined = [1, True, "apple"];

print(type(list1))
print(type(list2))
print(type(list3))
# Create list
thisList2 = list(("apple", "banana", 1, True, False, 123123))

# Access list items
thisList3 = ["apple", "banana", "cherry", "apple"]
print(thisList3[0])  # First elem
print(thisList3[-1])  # Negative indexing
print(thisList3[2:5])  # return 3,4,5 elem in list
print(thisList3[:4])  # return 1,2,3,4 elem in list :4 is starting from 0 to 4
print(thisList3[2:])  # return from 2 until the end

# Change list items
thisList3[1] = "grapefruit"
print(thisList3)
thisList3[1:3] = ["blackcurrant", "grapefruit"]
print(thisList3)
thisList3.insert(2, "watermelon")
print(thisList3)

# Add list items
thisList3.append("orange")
print(thisList3)
newList = []
thisList3.extend(list2)
newList.extend(thisList3)  # Extend can update new list with tuple sets dict
print(newList)

# Remove List items
thisList4 = ["apple", "banana", "cherry"]
thisList4.remove("cherry")
print(thisList4)
thisList4.pop(1)
print(thisList4)
thisList4.pop()
print(thisList4)
del thisList4
# Loops
thislist = ["apple", "banana", "cherry"]
for x in range(len(thislist)):
    print(thislist[x])

print("--------")
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
thislistLoop = [1, 2, 3, 4, 5, 6, 7]

[print(x) for x in thislistLoop]

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
# or
new1list = [x for x in fruits if "a" in x]
print(new1list)

# Sorting list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
numList = [11, 22, 33, 4, 5, 6, 7, 8, 9, 10]
numList.sort(reverse=True)
print(numList)

# Copy lists
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
