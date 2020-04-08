def merge(A,p,q,r):
	n1 = q - p + 1
	n2 = r - q
	L = []
	R = []
	for ii in range(n1):
		L.append(A[p+ii])
	for ii in range(n2):
		R.append(A[q+1+ii])
	ii = 0
	jj = 0
	kk = p
	while(ii<n1 and jj<n2):
		if(L[ii]<=R[jj]):
			A[kk] = L[ii]
			ii += 1
		else:
			A[kk] = R[jj]
			jj += 1
		kk += 1
	while(ii<n1):
		A[kk] = L[ii]
		ii += 1
		kk += 1
	while(jj<n2):
		A[kk] = R[jj]
		jj += 1
		kk += 1

def merge_sort(A,p,r):
	if(r>p):
		q = (p+r)//2
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		merge(A,p,q,r)

			

if __name__ == '__main__':
	
	arr = [12,11,13,5,6,7,1]
	n = len(arr)
	print('Unsorted : ', arr)
	merge_sort(arr,0,n-1)
	print('\nSorted : ')
	for ii in range(n):
		print(arr[ii])