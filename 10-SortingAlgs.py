#* Binary Search in python
__author__='Metehan Özcan'




def binarySearch(list, target):
    """_summary_

    Args:
        list (arr): sorted list contains integers
        target (int): target number that we are looking for
        

    Returns:
        int: returns index of target_
    """
    low =0
    high=len(list)-1
    
    #* Repeat until the low and high meet each other
    while low <= high:

        mid = low + (high - low)//2 #* find mid

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1




# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]
    

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
    
    array = [3, 4, 5, 6, 7, 8, 9]
    x = 4
    print(binarySearch(array,6))
