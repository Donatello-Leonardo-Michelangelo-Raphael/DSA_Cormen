import math

def find_max_crossing_subarray(A,low,mid,high):
	left_sum = -math.inf
	sum = 0
	for ii in range(mid,low-1,-1):
		sum = sum + A[ii]
		if(sum>left_sum):
			left_sum = sum
			max_left = ii
	right_sum = -math.inf
	sum = 0
	for ii in range(mid+1,high+1):
		sum = sum + A[ii]
		if(sum>right_sum):
			right_sum = sum
			max_right = ii
	return [max_left, max_right, left_sum+right_sum]


def find_max_subarray(A,low,high):
	if(high==low):
		return [low,high,A[low]]
	else:
		mid = int((low+high)/2)
		[left_low,left_high,left_sum]    = find_max_subarray(A,low,mid)
		[right_low,right_high,right_sum] = find_max_subarray(A,mid+1,high)
		[cross_low,cross_high,cross_sum] = find_max_crossing_subarray(A,low,mid,high)
	if(left_sum>=right_sum and left_sum>=cross_sum):
		return [left_low,left_high,left_sum]
	elif(right_sum>=left_sum and right_sum>=cross_sum):
		return [right_low,right_high,right_sum]
	else:
		return [cross_low,cross_high,cross_sum]


if __name__ == '__main__':

	A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
	n = len(A)
	[low,high,sum] = find_max_subarray(A,0,n-1)
	print('Low : ',low)
	print('High : ',high)
	print('Sum : ',sum)