import numpy as np

def next(A,curr_pntr):
	curr_pntr = A[0,curr_pntr]
	return int(curr_pntr)

def prev(A,curr_pointer):
	curr_pointer = A[2,curr_pointer]
	return int(curr_pointer)

def LIST_SEARCH(A,key,init_pointer):
	curr_pointer = init_pointer
	if(key==A[1,curr_pointer]):
		return curr_pointer
	
	while(next(A,curr_pointer)>=0):
		if(key==A[1,next(A,curr_pointer)]):
			return next(A,curr_pointer)
		else:
			curr_pointer = next(A,curr_pointer)

	return 'not found'


def LIST_INSERT(A,key,head_pointer):
	for ii in range(len(A[1,:])):
		if(A[0,ii]==0 and A[1,ii]==0 and A[2,ii]==0):
			A[0,ii] = head_pointer
			A[1,ii] = key
			A[2,ii] = -1
			A[2,head_pointer] = ii
			head_pointer = ii
			return head_pointer
	
	print('no space')


def LIST_DELETE(A,del_pointer):
	if(A[0,del_pointer]==-1):
		A[0,prev(A,del_pointer)] = -1
		A[0,del_pointer] = 0
		A[1,del_pointer] = 0
		A[2,del_pointer] = 0
	elif(A[2,del_pointer]==-1):
		A[2,next(A,del_pointer)] = -1
		A[0,del_pointer] = 0
		A[1,del_pointer] = 0
		A[2,del_pointer] = 0
	else:
		A[0,prev(A,del_pointer)] = next(A,del_pointer)
		A[2,next(A,del_pointer)] = prev(A,del_pointer)
		A[0,del_pointer] = 0
		A[1,del_pointer] = 0
		A[2,del_pointer] = 0



if __name__ == '__main__':

	A = np.zeros((3,7))
	A[:,1] = [2,4,4]
	A[:,2] = [-1,1,1]
	A[:,4] = [2,16,6]
	A[:,6] = [4,9,-1]
	head_pntr = 6
	print(A)
	head_pntr = LIST_INSERT(A,121,head_pntr)
	print(A)
	print(head_pntr)
	head_pntr = LIST_INSERT(A,344,head_pntr)
	print(A)
	print(head_pntr)
	LIST_DELETE(A,2)
	print(A)