import math

def max_subarray(A):
	n = len(A)
	max_sum = -math.inf
	low = 0
	high = 0
	for ii in range(n):
		sum = 0
		for jj in range(ii,n):
			sum = sum + A[jj]
			if(sum>max_sum):
				low = ii
				high = jj
				max_sum = sum
	return [low,high,max_sum]


if __name__ == '__main__':

	A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
	[low,high,sum] = max_subarray(A)
	print('Low : ',low)
	print('High : ',high)
	print('Sum : ',sum)