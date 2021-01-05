import numpy as np 

n,m,p = map(int,input().split())
a = np.array([input().split() for i in range(n)],int)
b = np.array([input().split() for j in range(m)],int)

print(np.vstack([a, b]))
