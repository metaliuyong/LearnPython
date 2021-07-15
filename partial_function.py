import functools


def add(a, b):
    return a + b


if __name__ == "__main__":
    add_3 = functools.partial(add, 3)
    print("add_3(7) = {}".format(add_3(7)))
