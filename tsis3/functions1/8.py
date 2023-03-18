nums = list(map(int, input().split()))
def has_007(nums):
    for i in range (len(nums)-1):
        if (nums[i] == 0 and nums[i+1]==0 and nums[i+2]==7 ):
            return True
             
        else:
            return False

if has_007(nums):
    print('True')
else:
    print('False')