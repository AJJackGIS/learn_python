list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

data = [
    {"name": "xxx", "age": 18},
    {"name": "xxxx", "age": 20},
    {"name": "xxxxx", "age": 15},
    {"name": "xxxxxx", "age": 60},
    {"name": "xxxxxxx", "age": 42},
]

# list.append(11)
list.extend([11])
print(list)

list.sort(reverse=True)

print(list)

data.sort(key=lambda x: len(x["name"]), reverse=True)

print(data)
