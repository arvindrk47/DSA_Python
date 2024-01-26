class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp = list(magazine)
        for char in ransomNote:
            if char in temp:
                temp.remove(char)
            else:
                return False
        return True
        
        