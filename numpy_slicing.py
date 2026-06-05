import numpy as np
a = np.array([
    [100,95, 120],       
    [120, 90, 89],       
    [89, 80, 98]        
])
print(a[-2])
print(a[-1,0:2])

# printing columns
print(a[:,1:3])