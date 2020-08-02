# string partition

s="Happy New Year 20"

a,b,c = s.partition("New Year")

print(a, b, c)

a = "The quick brown fox jumps over the lazy dog" #pangram contain all 26 alphabets

lst = a.split()

print("index of 'brown' {}".format(a.index("brown"))) # start index of brown

# count the occurences

cnt = a.lower().count('the')

print("occurences of 'the' in ignore case {}".format(cnt))

# check membership of element

print("quick" in a)

print("fox" not in a)

# del, remove elements
s = "Jackdaws love my big sphinx of quartz"

lst = s.split()

del lst[1] #deleted love

print(lst)

lst.remove('sphinx')

print(lst)

# deleting using index

del lst[lst.index('big')]

print(lst)

#lst.remove('pyramid') # error because pyramid is not in list

# insert element at specific place

lst.insert(2, "big")
print(lst)

# adding two list

lst1 =[1,2,3]
lst2 = [3,4,5]

lst3 = lst1+lst2 # using +
print(lst3)

lst3.extend([8,9,10]) # using extend
print(lst3)

#Reversing the list

s1 = "hello my name is devashish"
lst = s1.split()
print(lst)
lst.reverse()
print(lst)
print(" ".join(lst))

# Sorting list

a = [30,50,10,100,70,60,90,80,60]
b = a.copy()
a.sort() # Ascending
print(a)

b.sort(reverse=True)
print(b)

# Important sorting by len
s2 = "I do not know where family doctors acquired illegibly perplexing handwriting nevertheless, extraordinary pharmaceutical intellectuality counterbalancing indecipherability, transcendentalizes intercommunication' s incomprehensibleness."
lst = s2.split()
lst.sort(key=len, reverse=True)
print(lst)

# Sorted return sorted list and reversed returns iterator

c = [2, 9, 4, 1]
print(c)
d = sorted(c)
print(d)

e = reversed(c)
print(type(e))
print(list(e))