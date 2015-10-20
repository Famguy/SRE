import numpy as np
# SVD-RD for Row Downdate

def rowdowndate(A, q):
# Input: U, S, V, k and q
# k : Rank approximation given (one more than actual value) : int
# q : Number of rows to be downdated (one more than actual value) : int
# S (k*k) : diagonal matrix containing top k singular values of A : numpy array
# U (m*k), V (n*k) : corresponding left and right singular vectors of A : numpy arrays
# A = USVt 
	U, S, V = np.linalg.svd(A)
	m = U.shape[0]+1 # V.shape[1]
	k = S.shape[0]+1

	D = U[m-q+1:m,1:k]
	C = np.dot(D,S)
	B = S-np.dot(D.T,C)
	X, Y, Z = np.linalg.svd(B, full_matrices=True)
	U1 = np.dot(U[1:m-q,1:k],X[:,1:k])
	S1 = Y[1:k,1:k]
	V1 = np.dot(V,Z[:,1:k])

	R = np.dot(U1,S1)
	R1 = np.dot(R,V1.T)
	Z = np.zeros((q,R1.shape[1]))
	R2 = np.vstack([R1,Z])
	return R2



# for i in range(10):
# 	A1 = np.random.randint(0,200,size=(768,576))
# 	print A1
# 	print rowdowndate(A1,2)



