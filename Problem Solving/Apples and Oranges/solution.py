#!/bin/python3


def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples = 0
    total_oranges = 0

    for apple in apples:
        if s <= a+apple <= t:
            total_apples += 1

    for orange in oranges:
        if s <= b+orange <= t:
            total_oranges += 1

    print(total_apples)
    print(total_oranges)


if __name__ == '__main__':

    s,t = map(int, input().split(" "))

    a,b = map(int, input().split(" "))

    m,n = map(int, input().split(" "))

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)