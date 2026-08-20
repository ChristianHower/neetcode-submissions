class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        noSpace = s.lower()
        start = 0
        end = len(noSpace) - 1
        while start < end:
            if (noSpace[start] == noSpace[end]):
                start += 1
                end -= 1
            elif (noSpace[start].isalnum() == False):
                start += 1
            elif (noSpace[end].isalnum() == False):
                end -= 1
            else:
                print(noSpace[start])
                print(noSpace[end])
                return False
        return True
