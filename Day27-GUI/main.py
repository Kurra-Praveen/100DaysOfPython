def add(*args):
    """

    :type args: object
    """
    x = 0
    for n in args:
        x += n
    return x


print(add())
