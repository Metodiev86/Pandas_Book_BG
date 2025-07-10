import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])    # форма (2, 3)
b = np.array([[10], [20], [30]])       # форма (3, 1)

# Опит за поелементно събиране
result = a + b

#ValueError: operands could not be broadcast together with shapes (2,3) (3,1)