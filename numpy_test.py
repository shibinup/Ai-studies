import numpy as np
print(np.__version__)
a =np.array([1,2,3])
print(a)
print("\n")
b= np.array([[2,9,8],[2,3,2]])
b[1,2]=39
print(b)
print(np.sort(b,axis=None))
for row in b:
    print(row)