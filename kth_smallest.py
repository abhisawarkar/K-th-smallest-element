def kthSmallest(arr,low,high,k):

	if k>0 and k<=high-low+1:
		pos=partition(arr,low,high)			# find position to split
	
		if pos-low == k-1:
			return arr[pos]
		if pos -low > k-1:
			return kthSmallest(arr,low,pos-1,k)		# check left side 
		return kthSmallest(arr,pos+1,high,k-(pos-low)+1)	# check right side
	

def partition(arr,low,high):		# Partition into two halves by pivot
	wall = low-1
    	pivot = arr[high]     
    	for j in range(low , high):
        	if   arr[j] <= pivot:
        	    wall += 1					# move wall
        	    arr[wall],arr[j] = arr[j],arr[wall]		# Swap values less than pivot to sort rest of list
 
    	arr[wall+1],arr[high] = arr[high],arr[wall+1]		# Sawap to plcae pivot to front of wall
    	return wall+1

