import numpy as np

# a = np.reshape(np.array([range(1, 13)]), (2, 2, 3))
# # a = np.ones((2, 2, 3))
# # b = np.ones((2, 3, 4))
# b = np.array([[[1., 2., 3., 4.], [1., 2., 3., 4.], [1., 2., 3., 4.]], [[1., 2., 3., 4.], [1., 2., 3., 4.], [1., 2., 3., 4.]]])
# c = np.zeros((2, 4))

# print(a)
# print(b)

# for i in range(2):
#     for j in range(4):
#         temp = 0
#         for i_1 in range(2):
#             for i_2 in range(3):
#                 temp += a[i, i_1, i_2] * b[i, i_2, j]
#         c[i, j] = temp
        
# print(c)

a = np.array([[-1, 1, 2]]).T
print(np.eye(3)-2*a@a.T/3)

