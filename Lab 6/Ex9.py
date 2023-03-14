def base10to16(n):
    _list = []
    while n > 0:
        _list.append(n % 16)
        n //= 16
    _list.reverse()
    return "".join(str(i) for i in _list)

print(base10to16(1000))