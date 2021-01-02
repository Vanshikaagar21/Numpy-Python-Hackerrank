import numpy

n = int(input())

a = numpy.array([input().split() for i in range(n)], float)

a = numpy.linalg.det(a)
print(round(a, 2))
