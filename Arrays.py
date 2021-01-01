import numpy
arr = input().strip().split(' ')


def arrays(arr):
    return numpy.array(arr[::-1], float)


result = arrays(arr)
print(result)