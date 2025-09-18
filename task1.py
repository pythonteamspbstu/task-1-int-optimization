import sys

def solution(a,b):

    for i in range(a, b):
        if id(i) != id(i):
            return i
    return -1

print(solution(-1000000, 1000000))

