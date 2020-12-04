import numpy as np

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = data * 2
print(result, type(result))

x = np.array(data)
print(x, type(x))

result = x + 2
print(result, type(result))

print(x * 2, x // 2)

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
result = 2 * a + b
print(result , type(result), result.ndim) # ndim은 차원을 뜻함

#ex) b = np.array([[10,20,30],[10,20,30]])을 하면 2차원의 행렬을 뜻함