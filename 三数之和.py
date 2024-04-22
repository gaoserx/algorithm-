def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        n = len(nums)
        sum = 0
        ans = []
        for first in range(n):
            
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            second = first + 1
            third = n - 1
            while third > second:
                sum = nums[third] + nums[second] + nums[first]
                if sum > 0:
                    third -= 1
                elif sum < 0:
                    second += 1
                else:
                    ans.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while nums[second] == nums[second - 1] and second < third:
                        second += 1
                    while nums[third] == nums[third + 1] and second < third:
                        third -= 1
        return ans

list = [-1, 0, 1, 2, 4, 1, -6]
print(threeSum(nums = list))
