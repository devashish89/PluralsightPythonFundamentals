nums = [1,2,3]
#way1
i_nums = nums.__iter__()
print(type(i_nums))
print(dir(i_nums))

print(i_nums.__next__())
print(next(i_nums))

#way2
iterable = ["Spring", "Summer", "Autumn", "Winter", "Halo"] # Last next(iterator) - StopIteration Error
iterable1 = [] # Empty : ValueError
iterator = iter(iterable) # iter func returns iterator

while True:
    try:
        item = next(iterator)
        print(item)
    except (StopIteration, ValueError):
        break

print("-"*50)

def gen123():
    yield 1
    yield 2
    yield 3

g = gen123() #g is generator

print(next(g))
print(next(g))
print(next(g))

print("."*50)

for v in gen123():
    print(v)

print("."*50)

def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to leave func")

g = gen246()

print(next(g))
print(next(g))
print(next(g))
#print(next(g))

print("-"*50)

#Generator has not filled my RAM as they generate on the fly and after that RAM is free

def gen_nums(n):
    for i in range(n):
        yield i

def fibonacci(num):
    if (num <= 1):
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)


for i in range(10):
    print(fibonacci(i))

print("*"*50)

# Fibonacci series as generator 

def fib_gen():
    a=0
    b=1
    while True:
        f = a+b
        a=b
        b=f
        yield f

genObj = fib_gen()

for i in range(10):
    print(next(genObj))

