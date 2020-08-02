# dictionary mutable and unordered key value pair
#keys are immutable
#values are mutable


dic = {"google":"https://www.google.com/",
       "facebook":"https://www.facebook.com/",
       "pluralsight":"https://app.pluralsight.com/"}

print(dic["google"])

dic = dict((("dev", 30), ("ram", 20), ("shyam", 34))) #tuples<tuples>
print(dic["shyam"])

# shallow copy of dictionary

#way1

dic = dict(a="apple", b="ball", c="call")
print(dic)

dic1 = dic.copy()

print("dic is dic1: "+ str(dic is dic1))

#way2

dic2 = dict(dic)

print("dic is dic2: "+ str(dic is dic2))

##########################################

# add additional elements to dictionary
dic = dict((("dev", 30), ("ram", 20), ("shyam", 34)))
print(dic)
dic1 = dict(mohan=31, sohan=43)
dic.update(dic1)
print(dic)

## Iterate over dictionary ####

for key in dic:
    print("{} --> {}".format(key, dic[key]))

print("*"*50)
# way2

for key in dic.keys():
    print( "{} --> {}".format( key, dic[key] ) )

print("-"*50)
#way3

for key, value in dic.items():
    print("{} => {}".format(key, value))

# only values
for val in dic.values():
    print(val)


## check membership of key in dictionary

print("dev" in dic.keys())

## delete key and value pair from dictionary

del dic["sohan"]

print(dic)

print("^"*50)

## much nicer display of dictionary

from pprint import pprint as pp
pp(dic)

