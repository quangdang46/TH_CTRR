def base10to2(n):
    _list = []
    while n > 0:
        _list.append(n % 2)
        n //= 2
    _list.reverse()
    return "".join(str(i) for i in _list)

print(base10to2(6))