def outer(): # nested function for enclosing scope
    x="enclosing" # x has enclosing scope
    print(x)
    def inner():
        nonlocal x
        x = "local" # x has enclosing scope now becoz of nonlocal x statement
        print(x) ##2.) -- local
    inner()
    print(x) ##3.) -- local

outer()