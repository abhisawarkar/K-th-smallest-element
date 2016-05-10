def kthSmallest(arr,low,high,k):

	if k>0 and k<=high-low+1:
		pos=partition(arr,low,high)
	
		if pos-low == k-1:
			return arr[pos]
		if pos -low > k-1:
			return kthSmallest(arr,low,pos-1,k)
		return kthSmallest(arr,pos+1,high,k-(pos-low)+1)
	

def partition(arr,low,high):
	wall = low-1
    	pivot = arr[high]     
    	for j in range(low , high):
        	if   arr[j] <= pivot:
        	    wall += 1
        	    arr[wall],arr[j] = arr[j],arr[wall]
 
    	arr[wall+1],arr[high] = arr[high],arr[wall+1]
    	return wall+1

