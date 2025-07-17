class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        s = nums[0]
        nums.append(float('inf'))

        ans =[]

        for i in range (1, len(nums)):

            if nums[i] - nums[i-1] > 1:

                e = nums[i - 1]
                if s == e:
                    ans.append(str(s))
                else:
                    ans.append(f"{s}->{e}")

                s = nums[i]

        return ans      
