def do_and(x, y):
    return x & y


def do_lshift(x, n):
    return x << n


def do_not(x):
    return x ^ 65535


def do_or(x, y):
    return x | y


def do_rshift(x, n):
    return x >> n
