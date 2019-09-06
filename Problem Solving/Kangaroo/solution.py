#!/bin/python3


def kangaroo(x1, v1, x2, v2):

    if x1 == x2 and v1 == v2:
        return "YES"

    elif x1 == x2 and v1 != v2:
        return "NO"

    elif x1 <= x2 and v1 <= v2:
        return "NO"

    elif (x2-x1)%(v1-v2) == 0:
        return "YES"

    else:
        return "NO"


if __name__ == '__main__':

    x1,v1,x2,v2 = map(int,input().split(" "))

    result = kangaroo(x1, v1, x2, v2)

    print(result)