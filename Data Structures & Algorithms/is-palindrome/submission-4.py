class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = s.lower()
        l,r = 0 , len(str1)-1

        while l < r:
            
            while l < r and not str1[l].isalnum():
                l+=1        
                
            while r > l and not str1[r].isalnum():
                r-=1
            

            if str1[l] != str1[r]:
                print(l, r)
                print(str1[l], str1[r])
                return False
            
            l, r = l + 1, r - 1
        
        return True

        
