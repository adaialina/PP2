nums = list(map(int, input().split()))
def has_33(nums):
    for i in range (len(nums)-1):
        if (nums[i] == 3 and nums[i+1]==3 ):
            return True     
        else:
            return False

if has_33(nums):
    print('True')
else:
    print('False')