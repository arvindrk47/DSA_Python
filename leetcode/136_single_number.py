class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            if num in temp:
                temp.remove(num)
            else:
                temp.append(num)
        return temp[0]