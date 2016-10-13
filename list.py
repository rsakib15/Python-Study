li = ["cat ", "rat", "mouse", 1.26, 2]

print(li)  # print all the list values

# getting individual value in a list with indexes
print(li[0])
print(li[1])
print(li[2])
print(li[-1])  # -1 index represent the last value of the list

# list can contain other list values
list_two = [["cat", "bat"], 1, 2, 3]
print(list_two[0])
print(list_two[0][0])
print(list_two[0][1])
print(list_two[1])
print(list_two[2])

# negative indexes
print(li[-1])
print(li[-2])
print(li[-3])

# changing value of list
li[0] = "tiger"
li[0] = "lion"
print(li)

# list Concatenation
li = li + list_two
print(li)

spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

# delete list item
del spam[2]
print(spam)

