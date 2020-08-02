def outer():
    x="enclosing" # x has enclosing scope
    def inner():
        global x
        x = "local" # x has global scope now becoz of global x statement
        print(x) ##2.) -- local
    inner()
    print(x) ##3.) -- enclosing

try:
    print(x) ##1.) throw error
except NameError as e:
    print(e)
finally:
    outer()
    print(x) ##4.) -- local