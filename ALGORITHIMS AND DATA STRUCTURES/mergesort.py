"""
    merge sort is a pretty fast algo with a worst case of O(nlog n) the mergesort
    function should take in a list/array and split it untill its left with single
    item lists then return a merged& sorted list to the caller untill the last call
    which would return a sorted list
    
"""

nums = [28,53,55,1,2,3,8,15,8,7]
def mergesort(nums):
    if len(nums)<=1:
        return nums
    print('returned numbers--->',nums)
    middle= len(nums)//2
    right_half = mergesort(nums[middle:])
    left_half = mergesort(nums[:middle])
    print('left_half',left_half,right_half,'right_half')
    left_index = 0
    right_index = 0
    sorted_list = []

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_list.append(left_half[left_index])
            left_index +=1
        else:
            sorted_list.append(right_half[right_index]) 
            right_index +=1
            
    sorted_list += left_half[left_index:]
    sorted_list += right_half[right_index:]
    print('sorted_list--->',sorted_list)
    return sorted_list


mergesort(nums)
