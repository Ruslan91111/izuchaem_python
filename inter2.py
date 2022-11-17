def intersect(*args):
    res=[]
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break

        else:
            res.append(x)
    return res

def union(*args):
    res=[]
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res


def tester(func, items, trace=True):
    for i in range(len(items)):
        items[1:]+items[:1]
        if trace: print(items)
        print(sorted(func(*items)))





