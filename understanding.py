x = 10
y = 19.423
z = 54j
num = 10>9

print(type(x))
print(x)
print(type(y))
print(y)
print(type(z))
print(z)
print(type(num))
print(num)
#print should be used individually for checking the type


x = "Hello"
print(x)
print(type(x))
print(x[1])
#index numbers start from 0


fruits = ["apple","mango","banana","kiwi"]
print(fruits)
print(type(fruits))
fruits.append ('orange')
fruits.insert (2, 'tomato')
print(fruits)
#while appending or inserting any string value, use siingle inverted commas and space


animals = {'reptiles':'snake',
            'mammals':'whale',
            'amphibians':'frogs'
        }
print(animals)
print(type(animals))
animals ['water animals'] = ('fishes')
print(animals)
#remember 34th step for adding anything


Land_animals = ('lion','tiger','monkey')
print(type(Land_animals))
print(Land_animals)
print(Land_animals[1])
#don't use space while writing names. Use underscore instead


set = {10, 20, 30, 'courses', 30, 40}
print(set)
print(type(set))

from collections import namedtuple 
a = namedtuple('courses','name , technology')
s = a('data science','python')
print(s)


from collections import deque 
a = ['name','tech','python','course']
d = deque (a)
print(d)
#only two collection data types can be put at a time.

import array as arr
a = arr.array('i',[1,2,3,4,5,6])
print(a)


a = 90 
b = 60 
if a == b:
    print ("false")
elif a < b:
    print ("nope")
else:
    print ("true")


v = 30
c = 45
if v < 35 and c >50:
    print("first is correct")
elif v == 30 and c < 50:
    print("second is correct")
else:
    print("third is correct")



