book = {'name': 'Python Learing', 'type': 'Python'}
print(book['name'])
print(book['type'])

# print all the keys
for v in book.keys():
	print(v)
# print all the values of keys
for k in book.values():
	print(k)

... == == == == == == == == == == == ==
"List Vs Distionary"
== == == == == == == == == == == == ...
spam = ['cats', 'dogs', 'mouse']
bacon = ['dogs', 'mouse', 'cats']
print(spam == bacon)  # it return false . Order of item matter whether two list are same or not

personOne = {'name': 'john doe', 'age': 8, 'birthday': '10-05-1995'}
personTwo = {'birthday': '10-05-1995', 'name': 'john doe', 'age': 8}

print(personOne == personTwo)  # it return true . Order of items doesn't matter whether two dictionaries are same or not
