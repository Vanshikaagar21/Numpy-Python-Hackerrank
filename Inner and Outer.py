import numpy

A = numpy.array(input().split(),int)
B = numpy.array([input().split()],int)

a = numpy.inner(A, B)
print(*a)
print(numpy.outer(A, B))
