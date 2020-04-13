def init_pointer(A):
	pointer = {}
	for ii in range(len(A)):
		pointer[ii] = A[ii]
	return pointer

def pointer_next(pntr,initial_pointer):
	if(pntr>=len(initial_pointer)-1 or pntr<0):
		return 'error'
	else:
		return initial_pointer[pntr+1]

def pointer_prev(pntr,initial_pointer):
	if(pntr>len(initial_pointer)-1 or pntr<=0):
		return 'error'
	else:
		return initial_pointer[pntr-1]

def LIST_SEARCH(S,key,initial_pointer):
	x = False
	for k,v in initial_pointer.items():
		if(v==key):
			return k
	return x

def LIST_INSERT(S,key,initial_pointer):
	n = len(initial_pointer)
	initial_pointer[n] = key
	temp_pointer = initial_pointer.copy()
	for ii in range(n):
		initial_pointer[ii+1] = temp_pointer[ii]
	initial_pointer[0] = key
	m = len(S)
	S.append(key)
	temp_S = S.copy()
	for ii in range(m):
		S[ii+1] = temp_S[ii]
	S[0] = key
	

def LIST_DELETE(S,pntr,initial_pointer):
	temp_pointer = initial_pointer.copy()
	initial_pointer.pop(pntr)
	n = len(initial_pointer)
	for ii in range(pntr,n):
		initial_pointer[ii] = temp_pointer[ii+1]
	initial_pointer.pop(n)
	temp_S = S.copy()
	S.pop(pntr)
	n = len(S)
	for ii in range(pntr,n):
		S[ii] = temp_S[ii+1]
	



if __name__ == '__main__':

	A = [9,16,4]
	pointer = init_pointer(A)
	print(pointer)
	LIST_INSERT(A,91,pointer)
	print(pointer)
	print(A)
	LIST_DELETE(A,1,pointer)
	print(pointer)
	print(A)
