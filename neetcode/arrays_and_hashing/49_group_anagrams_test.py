class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        known_anagrams = {}
