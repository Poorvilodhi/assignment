print("1. To add two matrix")
X = [[12,7,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[5,8,1],
	[6,7,3],
	[4,5,9]]

result = [[0,0,0],
		[0,0,0],
		[0,0,0]]

# iterate through rows
for i in range(len(X)):
# iterate through columns
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j]

for r in result:
	print(r)

print("----------------------------------------------------------------------------------")

print("2. To perform scalar multiplication of a matrix and a number")
N = 3
def scalarProductMat(mat, k):
	for i in range(N):
		for j in range(N):
			mat[i][j] = mat[i][j] * k
if __name__ == "__main__":
	mat = [[12, 8,3],
		   [4, 5, 6],
		   [7, 8, 9]]
	k = 9
	scalarProductMat(mat, k)
	print("Scalar Product Matrix is : ")
	for i in range(N):
		for j in range(N):
			print(mat[i][j], end=" ")
		print()

print("----------------------------------------------------------------------------")

print("3. program to perform multiplication of matrix and vector")

print("---------------------------------------------------------------------------------")

print("4. Program to multiply two matrices")

A = [[12, 7, 3],
	 [4, 5, 6],
	 [7, 8, 9]]

B = [[5, 8, 1],
	 [6, 7, 3],
	 [4, 5, 9]]

result = [[0, 0, 0],
		  [0, 0, 0],
		  [0, 0, 0]]
for i in range(len(A)):
	for j in range(len(B[0])):
		for k in range(len(B)):
			result[i][j] += A[i][k] * B[k][j]

for r in result:
	print(r)

print("------------------------------------------------------------------------------")

print("5. program to find inverse matrix X ")
'''import numpy as np

mat1 = [[12,7,3],
        [4,5,6],
        [7,8,9]]

matrix = np.array(mat1)

print(np.linalg.inv(matrix))'''

print("------------------------------------------------------------------------------------")

print("6. Write a program to find transpose matrix")
N = 3


def transpose(A, B):
	for i in range(N):
		for j in range(N):
			B[i][j] = A[j][i]

A = [ [5,8,1],
[6,7,3],
[4,5,9]]

B = A[:][:]
transpose(A, B)

print("Result matrix is")
for i in range(N):
	for j in range(N):
		print(B[i][j], " ", end='')
	print()