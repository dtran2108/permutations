def permute(nums):
    res = []
    _permuteHelper(nums, 0, res)
    return res

def _permuteHelper(nums, start, results):  #helper method
        if start >= len(nums):
            results.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                _permuteHelper(nums, start+1, results)
                nums[start], nums[i] = nums[i], nums[start]

nums = ['1', '2', '3']
print(permute(nums))