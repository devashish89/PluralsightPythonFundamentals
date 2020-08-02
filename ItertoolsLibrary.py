import itertools
# all - AND for list<bool>
print(all([name == name.title() for name in ["London", "New York", "United States Of America"]])) #name.title() - all initial letters of words in upper case

#any - OR for list<bool>
print(any([x for x in range(10) if x%2==0]))

# zip - merge lists horizontally

mon = [10, 12, 14, 15, 21]
tues = [11, 21, 18, 20, 21]
wed = [22, 23, 20, 17, 21]

for temp in zip(mon, tues, wed):
    print("max: {0:.3f}, min: {1:.3f}, avg: {2:.3f}".format(min(temp), max(temp), sum(temp)/len(temp)))

print('.'*50)

# chain - merge lists vertically into 1 list

temperatures = itertools.chain(mon, tues, wed)

print(temperatures)

for temp in temperatures:
    print(temp)
    

print("."*50)

# count and islice
"""
import time
x = itertools.count(1, 2) #Infinite loop starting from 1 and in step size of 2 (count backwards also using -1)

while True:
    print(next(x))
    time.sleep(2)

        
print("-"*50)
"""


# islice to chunk/slice iterator

for i in itertools.islice(itertools.count(1), 5): #print only first 5 values
    print(i)

print("*"*50)

for i in itertools.islice(itertools.count(10,-1), 5): #print only first 5 values
    print(i)

print("*"*50)

for i in itertools.islice(itertools.count(10,-1), 5, 10): #print values from 5th to 10th element
    print(i)

print("*"*50)

for i in itertools.islice(itertools.count(10,-1), 5, 10, 2): #print values from 5th to 10th element in step size=2
    print(i)