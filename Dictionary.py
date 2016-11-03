book = {'name': 'Python Learing', 'type': 'Python'}
print(book['name'])
print(book['type'])

# print all the keys
for v in book.keys():
	print(v)
# print all the values of keys
for k in book.values():
	print(k)
# print all the keys and values separtely
for k in book.items():
	print(k)

# List vs Dictionary

spam = ['cats', 'dogs', 'mouse']
bacon = ['dogs', 'mouse', 'cats']
print(spam == bacon)  # it return false . Order of item matter whether two list are same or not

personOne = {'name': 'john doe', 'age': 8, 'birthday': '10-05-1995'}
personTwo = {'birthday': '10-05-1995', 'name': 'john doe', 'age': 8}

print(personOne == personTwo)  # it return true . Order of items doesn't matter whether two dictionaries are same or not

# check whether the key exits or not

n = 'name' in personOne.keys()
print(n)

n = personOne.get('name', 'no name')
print(n)

# get method

picnicItems = {'apples': 5, 'cups': 10}
print(picnicItems.get('apples', 0))  # get the key value and if failed to retrieve then return the fallback

# set default value

cat = {'height': 5.6, 'weight': 3.6}
print(cat)
cat.setdefault('color', 'black')
print(cat)
cat.setdefault('color', 'white')
print(cat)

message = "this is going to be my new framework crush. The codebase seems clean and certainly a good starting point to learn about asynchronous programming for me "

countchar = {}

for character in message:
	countchar.setdefault(character, 0)
	countchar[character] = countchar[character] + 1

print(countchar)
