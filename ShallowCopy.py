a = [[1,2], [3,4]]

b = a[:] # shallow copy

print("memory loc of a:{} & memory loc of b:{}".format(id(a), id(b)))
print("a is b: "+ str(a is b))


print("a[0] is b[0]: "+ str(a[0] is b[0]))

a[0] = [5,6] # a[0] is reference to new memory location holding [5,6]

print("a[0] is b[0]: "+ str(a[0] is b[0]))

print(a)
print(b)

print("a[1] is b[1]: "+ str(a[1] is b[1]))

a[1].append(5)

print("a[1] is b[1]: "+ str(a[1] is b[1]))


print(a)
print(b)

print("@"*50)
# another way to create shallow copy

a=[[1,2], [3,4]]
b = a.copy()

print("a is b: "+ str(a is b))

print("a[0] is b[0]: "+ str(a[0] is b[0]))

a[0] = [8,9,10]

print("a[0] is b[0]: "+ str(a[0] is b[0]))

print(a)
print(b)



