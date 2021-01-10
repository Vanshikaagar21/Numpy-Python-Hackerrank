import numpy

n , m = map(int,input().rstrip().split())

a = numpy.array([input().split() for i in range(n)],int)

print(numpy.mean(a , axis = 1))
print(numpy.var(a , axis = 0))
a = numpy.std(a , axis = None)
print(round(a,11))
