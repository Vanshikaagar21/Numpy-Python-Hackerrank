import numpy

numpy.set_printoptions(legacy = '1.13')
a = list(map(float,input().rstrip().split()))
a = numpy.array(a)

print(numpy.floor(a)) 
print(numpy.ceil(a)) 
print(numpy.rint(a))

