import json
import random

print(random.random())
print(random.randrange(10))
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5, 6, 7]))
print(random.choice(range(100)))
print(random.choice('Runoob'))

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

# str = '{"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}'

print(type(json.dumps(data)))
# print(json.loads(str))

num = 1

print(str(num))

print(dict(a=1, b=2, c=3))

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

while True:
    x = next(it, "")
    print(x)
    if x == "":
        break

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1[slice(1, 5)])
print(list1)
list1.sort(key=lambda x: -x)
print(list1)
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2.sort(reverse=True)
# list2.reverse()
list3 = sorted(list2, key=lambda x: -x)
print(list2)
print(list3)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i, element in enumerate(seasons, start=1):
    print(i, element)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr1 = filter(lambda x: x % 2, arr)
print(arr, list(arr1))
