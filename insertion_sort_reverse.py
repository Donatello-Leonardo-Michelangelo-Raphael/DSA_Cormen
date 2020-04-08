def insertion_sort_reverse(A):
	for jj in range(len(A)-2,-1,-1):
		key = A[jj]
		ii = jj + 1
		while(ii<=len(A)-1 and A[ii]>key):
			A[ii-1] = A[ii]
			ii = ii + 1
		A[ii-1] = key
	return A

if __name__ == '__main__':

	A = [5,2,4,6,1,3]
	print('Unsorted : ', A)
	sorted_A = insertion_sort_reverse(A)
	print('Sorted : ', sorted_A)
