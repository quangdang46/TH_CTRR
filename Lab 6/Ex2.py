def primeFact(p):
    _list = []
    d = 2
    while d * d <= p:
        while (p % d) == 0:
            _list.append(d)
            p //= d
        d += 1
    if p > 1:
        _list.append(p)
    return _list

print(primeFact(60))