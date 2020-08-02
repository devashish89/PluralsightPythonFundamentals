import time

print(time.ctime())

count =0

def show_count():
    print(count)

def set_count(i):
    count = i # here count is local variable with scope within set_count() func

def set_count_global(i):
    global count # here count is global count which is initialized at top
    count = i



if __name__ == "__main__":
    set_count(5)
    show_count()

    print("-"*50)

    set_count_global(5)
    show_count()