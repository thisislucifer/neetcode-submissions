class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setList = set(nums)
        longest = 0
        numStart = 0
        

        for each_num in setList:
            
            if each_num-1 not in setList:
                length = 1
                while (each_num + length) in setList:
                    length += 1
                longest = max(length, longest)
        
        return longest
            

