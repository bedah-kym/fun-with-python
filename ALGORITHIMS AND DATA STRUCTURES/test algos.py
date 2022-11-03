import random
from random import randrange
lst=[]
for i in range (0,500):
    lst.append(randrange(23,500))
#lists=set(lst)
print (lst)

lst=[25,4,56,7,5,4,3,1,20]

def bubble_sort(nums):
    n= len(nums)
    for x in range(0,n):
        for i in range (1,n):
            print (nums)
            if nums[i-1] > nums[i]:
                temp=nums[i]
                nums[i]=nums[i-1]
                nums[i-1]=temp
                
            elif nums[i-1] <= nums[i]:
                pass
    return nums
        
print(" this is bubble",bubble_sort(lst))
        
    
