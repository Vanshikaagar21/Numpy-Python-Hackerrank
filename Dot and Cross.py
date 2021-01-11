import numpy

n = int(input())

a = numpy.array([input().rstrip().split() for i in range(n)],int)

b = numpy.array([input().rstrip().split() for j in range(n)],int)

print(numpy.matmul(a, b))
