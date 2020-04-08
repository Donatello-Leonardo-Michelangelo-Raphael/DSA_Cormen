def insertion_sort_recursive(A):
	jj = len(A)-1
	key = A[jj]
	ii = jj - 1
	if(len(A)>2):
		B = insertion_sort_recursive(A[0:jj])
		for kk in range(jj):
			A[kk] = B[kk]
		while(ii>=0 and A[ii]>key):
			A[ii+1] = A[ii]
			ii = ii - 1
		A[ii+1] = key
	else:
		while(ii>=0 and A[ii]>key):
			A[ii+1] = A[ii]
			ii = ii - 1
		A[ii+1] = key
	return A

if __name__ == '__main__':
	
	A = [5,3,4,6,1,2]
	print('Unsorted : ', A)
	insertion_sort_recursive(A)
	print('Sorted : ', A)
			