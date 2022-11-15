import numpy as np

data = list(map(int, input().split()))
a= np.array(data)
data = list(map(int, input().split()))
b= np.array(data)
print(np.inner(a,b))
print(np.outer(a,b))


