import sys
print(sys.getdefaultencoding())

with open("sample.txt", "rt", encoding="utf-8") as f:
    for line in f.readlines():
        print(line)

f = open("sample.txt", "at") # append mode
f.write("\nhello this is appended text")
f.write(" hello this is appended text")
f.close()

f = open("sample.txt", "at") # append mode
f.writelines(["ABC\n",
              "CDEF \n",
              "Ending the file...."])
f.close()

with open("sample.txt", "rt", encoding="utf-8") as f:
    for line in f.readlines():
        print(line)


f = open("wasteland.txt", "wt")
f.write("hello my name is devashish\n")
f.write("I'm doing good!")
f.close()


f = open("wasteland.txt", "rt")
print(f.read(10)) # read first 10 characters
print(f.read(10)) # read next 10 characters
print(f.read()) #read all remaining characters
f.seek(0) #move file pointer to first location
print(f.read())
f.close()

print("-"*50)

f = open("wasteland.txt", "rt")
print(f.readlines()) # read all lines and stores them in a list
f.close()

print("."*50)

#### read file ######

f = open("wasteland.txt", "rt")
for line in f:
    sys.stdout.write(line)
f.close()

############################
print("#"*50)

f = open("wasteland.txt", "rt")
print([line for line in f])
f.close()

############################
print("#"*50)
f = open("wasteland.txt", "rt") ##line.strip() removes \n
print([line.strip() for line in f])
f.close()


