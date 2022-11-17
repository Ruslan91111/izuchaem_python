def mymap(func, *seq):
    res=[]
    for i in zip(*seq):
        res.append(func(*i))
    return res



# использование спискового включения
def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]


def mymap(func,*seqs):
    for args in zip(*seqs):
        yield func(*args)


def mymap(func,*seqs):
    return (func(*args) for args in zip(*seqs))