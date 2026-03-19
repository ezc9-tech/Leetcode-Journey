class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #Simply returna a list of two destructed nums arrays
        return [*nums, *nums]