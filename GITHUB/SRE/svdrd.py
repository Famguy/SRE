import numpy as np
# SVD-RD for Row Downdate

def rowdowndate(U, S, V, k, q):
# Input: U, S, V, k and q
# k : Rank approximation given (one more than actual value) : int
# q : Number of rows to be downdated (one more than actual value) : int
# S : diagonal matrix containing top k singular values of A : numpy array
# U, V : corresponding left and right singular vectors of A : numpy arrays
# A = USVt 
	D = U[m-q+1:m,1:k]
	C = np.dot(D,S)
	B = S-np.dot(D.T,C)
	X, Y, Z = np.linalg.svd(B, full_matrices=True)
	U1 = np.dot(U[1:m-q,1:k],X[:,1:k])
	S1 = Y[1:k,1:k]
	V1 = np.dot(V,Z[:,1:k])
	return U1, S1, V1



