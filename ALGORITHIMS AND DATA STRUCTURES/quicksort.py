
def quicksort(nums):
    """in quicksort take a list and find a pivot which is an element inside the list
        for our example we will always use the first element as pivot.take the pivot
        and split it into two lists.the  list on the left will be elements less than the pivot
        and on the right elements greater than the pivot.call quicksort on this sub-lists
        untill they are sorted on either side then merge them together with the middle element
        being the pivot"""
    
    if len(nums) <=1:
        return nums
    greater_than_pivot =[]
    less_than_pivot =[]
    pivot = nums[0]
    for elem in nums[1:]:
        if elem >= pivot:
            greater_than_pivot.append(elem)
        else:
            less_than_pivot.append(elem)
    print("%15s %ls %-15s " % (less_than_pivot ,pivot ,greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot) #split the sublist untill you hit base case then it starts to return the lists 
    
numbers=[25,5,4,3,10,8,2,85,68,45]

names = ['bedan','michael','sparta','john','kelvin','barbra','mercy','njoki']

print(quicksort(names))
