class Solution(object):
    def permute(self, nums):
        res = []
        self._permuteHelper(nums, 0, res)
        return res

    def _permuteHelper(self, nums, start, results):  #helper method
            if start >= len(nums):
                results.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    nums[i], nums[start] = nums[start], nums[i]
                    self._permuteHelper(nums, start +1, results)
                    nums[start], nums[i] = nums[i], nums[start]

s = Solution()
nums = [1, 2, 3]
print(s.permute(nums))