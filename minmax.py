def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res



def min2(first, *rest):
    for arg in rest:
        if arg<first:
            first=arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

def minimax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg,res):
            res=arg
    return res


def lessthan(x,y): return x<y
def grtrthan(x,y): return x>y






