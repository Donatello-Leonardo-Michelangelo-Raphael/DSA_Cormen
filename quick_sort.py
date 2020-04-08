def QUICKSORT(A,p,r):
	if(p<r):
		q = PARTITION(A,p,r)
		QUICKSORT(A,p,q-1)
		QUICKSORT(A,q+1,r)

def PARTITION(A,p,r):
	x = A[r]
	ii = p-1
	for jj in range(p,r):
	 	if(A[jj]<=x):
	 		ii += 1
	 		temp = A[ii]
	 		A[ii] = A[jj]
	 		A[jj] = temp
	temp = A[ii+1]
	A[ii+1] = A[r]
	A[r] = temp
	return ii+1

if __name__ == '__main__':

	A = [2,8,7,1,3,5,6,4]
	QUICKSORT(A,0,len(A)-1)
	print(A)
