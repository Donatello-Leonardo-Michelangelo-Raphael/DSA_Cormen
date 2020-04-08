def PARENT(i):
	return int((i-1)/2)

def LEFT(i):
	return 2*i+1

def RIGHT(i):
	return 2*i+2

def MAX_HEAPIFY(A, i):
	l = LEFT(i)
	r = RIGHT(i)
	A_heapsize = len(A)

	if(l>=A_heapsize and r>=A_heapsize):
		pass
	elif(l<A_heapsize and r>=A_heapsize):
		if(l<=A_heapsize and A[l]>A[i]):
			largest = l
		else:
			largest = i
		if(largest!=i):
			temp = A[i]
			A[i] = A[largest]
			A[largest] = temp
			MAX_HEAPIFY(A, largest)
	elif(l>=A_heapsize and r<A_heapsize):
		if(r<=A_heapsize and A[r]>A[largest]):
			largest = r
		else:
			largest = i
		if(largest!=i):
			temp = A[i]
			A[i] = A[largest]
			A[largest] = temp
			MAX_HEAPIFY(A, largest)
	else:
		if(l<=A_heapsize and A[l]>A[i]):
			largest = l
		else:
			largest = i
		if(r<=A_heapsize and A[r]>A[largest]):
			largest = r
		if(largest!=i):
			temp = A[i]
			A[i] = A[largest]
			A[largest] = temp
			MAX_HEAPIFY(A, largest)

def BUILD_MAX_HEAP(A):
	A_heapsize = len(A)
	for ii in range(int(len(A)/2),-1,-1):
		MAX_HEAPIFY(A, ii)

def HEAP_SORT(A):
	sorted_A = [0]*len(A)
	BUILD_MAX_HEAP(A)
	for ii in range(len(A)-1,-1,-1):
		print(A,ii)
		max_elem = A.pop(0)
		sorted_A[ii] = max_elem
		MAX_HEAPIFY(A, 0)
	return sorted_A



if __name__ == '__main__':

	A = [4,1,3,2,16,9,10,14,8,7]
	sorted_A = HEAP_SORT(A)

	print(sorted_A)