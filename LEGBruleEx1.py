"""
###### LEGB Rule #########
L- local
E - enclosing
G - global
B - builtin
"""

x="global" # x has global scope

def outer():
    x="enclosing" # x has enclosing scope
    def inner():
        x = "local" # x has local scope
        print(x) ## -- local
    inner()
    print(x) ## -- enclosing

print(x)
outer()
print(x) ## -- global

