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


array = [3, 4, 5, 6, 7, 8, 9]
x = 4
print(binarySearch(array,6))