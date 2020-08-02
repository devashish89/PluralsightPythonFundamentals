f = [1,2,3]
def lst_display(g):
    print("memory loc of f: {} & memory loc of g: {}".format(id(f), id(g)))
    print("f is g: " + str(f is g))
    g = [4,5,6]
    print( "memory loc of f: {} & memory loc of g: {}".format( id( f ), id( g )))
    print(g)
    
print(f)

lst_display(f)


def lst_add(lst, n):
    lst.append(n)
    return lst

print(lst_add(f, 12))


def lst_modify(g):
    print( "memory loc of f: {} & memory loc of g: {}".format( id( f ), id( g ) ) )
    g[0] = "10"
    g[1] = 20
    print( "memory loc of f: {} & memory loc of g: {}".format( id( f ), id( g ) ) )
    return g

print(lst_modify(f))




    
    
