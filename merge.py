#merge sort function
def mergesort(arr):
    if len(arr) == 1:
        return 
    
    ##find mid of array
    mid= len(arr)//2

    #Divide array into left and right
    left=arr[:mid]
    right=arr[mid:]

    #recursively call the mergesort function on divided subarrays
    mergesort(left)
    mergesort(right)

    mergetwosortedlists(left,right,arr)

def mergetwosortedlists(l,r,arr):
    len_l= len(l)
    len_r = len(r)

    i=j=k=0

    #i,j are pointers of left and right subarrays respectively and k is the new array
    while i<len_l and j<len_r:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j +=1
        k += 1
    while i< len_l:
        arr[k] = l[i]
        i += 1
        k += 1
    while j< len_r:
        arr[k] = r[j]
        j += 1
        k += 1

ar = [15,2,1,3,5,6,22]
mergesort(ar)
print(ar)
