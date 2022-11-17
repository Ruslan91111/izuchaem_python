def myzip(*seqs):
    seq = [list(s)for s in seqs]
    res=[]
    while all(seqs):
        res.append(tuple(s.pop(0)for s in seqs))
    return res


def mymapPad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res



# генераторы

def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)

def mymapPad(*seqs, pad=None):
    seqs=[list (s) for s in seqs]
    while any(seqs):
        yield tuple((s.pop(0) if s else pad) for s in seqs)


# альт.реализация с использ.длин

def myzip(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple((s[i] for s in seqs) for i in range(minlen)]




def mymapPad(*seqs, pad=None):
    maxlen = max(len(s) for s in seqs)
    index = range(maxlen)
    return [tuple((s[i] if len(s) > i else pad) for s in seqs) for i in range(index)]