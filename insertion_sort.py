def insertion_sort(A):
	
	for jj in range(1,len(A)):
		key = A[jj]
		ii = jj - 1
		while(ii>=0 and A[ii]>key):
			A[ii+1] = A[ii]
			ii = ii - 1
		A[ii+1] = key
	return A

if __name__ == '__main__':
	
	A = [5,2,4,6,1,3]
	print('Unsorted : ', A)
	sorted_A = insertion_sort(A)
	print('Sorted : ', sorted_A)