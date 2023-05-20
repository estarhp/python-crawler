import numpy as np

# 创建数组a和y
a = np.array([[1.,2.],[3.,4.]])
y = np.array([[5.],[7.]])


print(a)


# (2) 输出数组a的转置
print(a.T)


# (3) 输出形状为(2,2)的对角矩阵b
b = np.diag((1.,1.))
print(b)


# (4) 输出对角矩阵的迹
trace_b = np.trace(b)
print("%.1f"%(trace_b))


# (5) 求解数组a和数组y的解
x = np.linalg.solve(a, y)
print(x)