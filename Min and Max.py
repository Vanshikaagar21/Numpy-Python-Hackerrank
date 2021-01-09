import numpy

n,m = map(int,input().split())

a = numpy.array([input().split() for i in range(n)],int)
a = numpy.min(a, axis = 1)
print(numpy.max(a))
