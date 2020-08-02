x = "global" #global scope

def outer():
    x = "enclosing"
    print(x) #2.1) - enclosing
    def inner():
        print(x) #2.2.) since in local scope of x is not there so it will look for enclosing scope for x value -- enclosing

    inner()
    print(x) #2.3.) --enclosing

print(x) #1.) --global
outer() #2.)
print(x) #3.) --global