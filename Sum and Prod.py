import numpy

n , m = list(map(int,input().rstrip().split()))

a = numpy.array([input().split() for i in range(n)],int)

a = numpy.sum(a, axis = 0)

print(numpy.prod(a, axis = None))
