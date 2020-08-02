# Sets are mutable
# Sets are unordered
# collection of unordered mutable types
s = set()
print(type(s))

s.add(1)
s.add(2)
s.add(1)
s.add(5)

print(s)

# add multiple elements to a set

s.update([2,44,44,5,7,89,8,0,9])
print(s)

# remove element from set

s.remove(8)
print(s)

s.discard(44)
print(s)

s.discard(100) # does not throw error if element not in set
print(s)

# s.remove(100) #throw error if element not in set

## shallow copy
k = s.copy()
print(k is s)

##Set Operations

black_eye = {"ram", "sohan", "mohan", "shyam"}
brown_hair = {"ram", "priya", "mohan", "deva"}
o_typeBlood = {"sohan", "mohan"}
ab_type = {"rohan", "rahul", "sudha"}

print("black eyes OR brown hair: ", black_eye.union(brown_hair)) # commutative
print("black eyes AND brown hair", black_eye.intersection(brown_hair)) # commutative
print("Only have black eye and no brown hair", black_eye.difference(brown_hair)) #non commutative
print("Only have brown hairs and no black eyes", brown_hair.difference(black_eye)) #non commutative
print("Only have black eyes OR Only have brown hair", black_eye.symmetric_difference(brown_hair)) # commutative

print("O blood type is subset of black eye: ", o_typeBlood.issubset(black_eye))
print("black eye is superset of O blood type: ", black_eye.issuperset(o_typeBlood))
print("Is black eye disjoint(nothing common) with ab_type: ", black_eye.isdisjoint(ab_type))
print("Is black eye disjoint(nothing common) with o_type: ", black_eye.isdisjoint(o_typeBlood))

