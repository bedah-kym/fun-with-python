"""
    this split function demonstrates recurssion by taking a list and dividing it in half
    into sub-lists untill we are left with single item lists .everytime the split function will be
    called and will split then call itself intill the length of the list is less than or == 1
"""


nums=[1,2,3,4,5,6,7,9,8]

def split(nums):
    if len(nums)<=1:
        return nums
    middle=len(nums)//2
    print('nums',nums)
    left_list=split(nums[:middle])
    right_list = split(nums[middle:])
    
    print("%15s %-15s" %(left_list,right_list))
    return left_list+right_list


print(split(nums))
            
"""
helo="hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
def greetings(greeting):
    if len(greeting) < 3 :
        return greeting
    print(greeting)
    response = greetings(greeting[:-1])
    return response

print(greetings(helo))

"""
