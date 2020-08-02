# Duck Typing: we don't care if obj is the isinstance of Duck()
# only thing we care about is that obj should behave like duck: quack() and fly() then it can be treated as Duck()

class Duck:
    def quack(self):
        print("quack")

    def fly(self):
        print("fly")

class Person:
    def quack(self):
        print("quack")

    def fly(self):
        print("fly")


def fly_and_quack(obj):
    if isinstance(obj, Duck):
        obj.quack()
        obj.fly()

    else:
        obj.quack()
        obj.fly()
        print("This has to be Duck!")

def fly_and_quackNon_Pythonic(obj):
    #asking for permission at every step
    if hasattr(obj, 'quack'):
        if callable(obj.quack):
            obj.quack()
    if hasattr(obj, "fly"):
        if callable(obj.fly):
            obj.fly()

def fly_and_quackPythonic(obj):
    #ask for forgiveness and not permission (EAFP: easy to ask for forgiveness than permission)
    try:
        obj.quack()
        obj.fly()
        obj.bark()
    except AttributeError as e:
        print(e)
        
d = Duck()
fly_and_quack(d)

p = Person()
fly_and_quack(p)

fly_and_quackPythonic(d)
fly_and_quackPythonic(p)

print("*"*50)

person1 =dict(name="Deva", age=20, job="Programmer")
# Non - Pythonic
if "name" in person1.keys() and "age" in person1.keys() and "job" in person1.keys():
    print("I'm {name}. I'm {age} years old and works as {job}".format(**person1))
else:
    print("missing some keys!")

person2 = dict(name="Deva", age=20)
#Pythonic way
try:
    print("I'm {name}. I'm {age} years old and works as {job}".format(**person2))
except KeyError as e:
    print(e)
    print("Missing a key:{}".format(e))



lst = [1,2,3,4,5]
#Non - Pythonic way
def print_list_byIndex(index):
    if index < len(lst):
        print(lst)
    else:
        print("Index is more than length of list")
print_list_byIndex(10)
#Pythonic way for list
try:
    print(lst[10])
except IndexError as e:
    print(e)


#Non - Pythonic way to handle file
import os
file1="wasteland1.txt"
if os.path.exists(file1):
    with open(file1, "rt") as f:
        print(f.read())
else:
    print("File does NOT exist")

# Python way to handle File
file2="wasteland2.txt"
try:
    with open(file2, "rt") as f:
        print(f.read())
except IOError as e:
    print(e)



