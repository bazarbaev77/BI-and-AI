import numpy as np

#1
# zeros= np.zeros(10)
# zeros[4] = 1
# print(zeros)

# #2
# s = np.arange(10, 50)  
# print(s)

#3
# s = np.arange(49, 9, -1)
# print(s)

#4
# matrix_range = np.arange(0, 9).reshape(3, 3)
# print(matrix_range)

#5
# array = np.array([1, 2, 0, 0, 4, 0])
# non_zero_indices = np.nonzero(array)[0]
# print(non_zero_indices)

#6
# identity_matrix = np.eye(3)
# print(identity_matrix)

#7
# matrix_range = np.arange(0, 9).reshape(3, 3)
# max = np.max(matrix_range)
# min = np.min(matrix_range)
# print(f"min = {min}, max = {max}")

#8
# array = np.array([1, 3, 5, 11, 15, 20, 25])
# target = 14
# num = array[np.abs(array-target).argmin()]
# print("Closest num:", num)

#9
# matrix = np.random.rand(5, 5)
# norm_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))
# print("Normalized Matrix:\n", norm_matrix)

#10
# array = np.array([[5, 9, 3], [10, 2, 15], [6, 7, 8]])
# array[np.arange(array.shape[0]), array.argmax(axis=1)] = 0
# print(array)

#11
# array = np.array([2, 3, 2, 5, 8, 3, 3, 7, 2, 3, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7 ,7,7 ,7, 7 ,7,7])
# unique, counts = np.unique(array, return_counts=True)
# most_common = unique[np.argmax(counts)]
# print("Most common value:", most_common)

#12
# array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrix_product = np.dot(array, array.T)
# print("Matrix product of array and its transpose:\n", matrix_product)

#13
# matrix = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
# determinant = np.linalg.det(matrix)
# print("Determinant: ", determinant)

#14
# matrix = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
# try:
#     inverse_matrix = np.linalg.inv(matrix)
#     print("Inverse of the matrix:\n", inverse_matrix)
# except np.linalg.LinAlgError:
#     print("Matrix is singular and cannot be inverted.")

