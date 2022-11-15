import numpy as np

#a=np.array([1,2])
#b=np.array([3,4])

# (1*3) + (2*4)

#resultado= np.dot(a,b)
#print(resultado)

#print()

#resultado=np.cross(a,b)
#print(resultado)

n= int(input())

data= [list(map(int, input().split())) for i in range (n)]

a= np.array(data)
print(a)
data= [list(map(int, input().split())) for i in range (n)]
b= np.array(data)
result=np.matmul(a,b)
print(result)