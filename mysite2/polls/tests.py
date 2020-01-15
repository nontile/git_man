from django.test import TestCase

# Create your tests here.
def test3(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)


def test(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


def test2(nba):
    print(nba)
    # for key, value in kwargs.items():
    #     print("{0} = {1}".format(key, value))


dicts = {"a": 1, "b": 2, "c": "c3"}
# test(**dicts)
# test2(dicts)
test(nba="ddd", age="CCC")
test2(nba="ddd")
# test3(**dicts)


