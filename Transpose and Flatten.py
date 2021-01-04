import numpy

d = list(map(int,input().rstrip().split()))
s = []

for i in range(d[0]):
  l1 = list(map(int,input().rstrip().split()))
  s.append(l1)
  
m = numpy.array(s).reshape(d[0],d[1])

print(numpy.transpose(m))
print(m.flatten())

  

  

