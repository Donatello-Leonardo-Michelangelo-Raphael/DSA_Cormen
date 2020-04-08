from heap_sort import *
import math

def HEAP_MAXIMUM(A):
	return A[0]

def HEAP_EXTRACT_MAX(A):
	if(len(A)<1):
		print("heap underflow")
		pass
	else:
		max_elem = A.pop(0)
		MAX_HEAPIFY(A,0)
		return max_elem

def HEAP_INCREASE_KEY(A,i,key):
	if(key<A[i]):
		print('new key is smaller than current key')
		pass
	else:
		A[i] = key
		while(i>0 and A[PARENT(i)]<A[i]):
			temp = A[i]
			A[i] = A[PARENT(i)]
			A[PARENT(i)] = temp
			i = PARENT(i)

def HEAP_INSERT(A,key):
	A.append(-math.inf)
	HEAP_INCREASE_KEY(A,len(A)-1,key)


if __name__ == '__main__':

	A = [15,13,9,5,12,8,7,4,0,6,2,1]
	HEAP_INSERT(A,10)
	print(A)
