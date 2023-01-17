class anagram:
    def isAnagram(self, s: str, t: str) -> bool:
       #the following line solves the problem with Memory O(1)
        #return sorted(s) == sorted(t)
        
        #return Counter(s) == Counter(t)
        
        if len(s)!= len(t):
            return False
        
        hm1, hm2 = {}, {}
        
        for x in range(len(s)):
            hm1[s[x]] = 1 + hm1.get(s[x], 0) 
            hm2[t[x]] = 1 + hm2.get(t[x], 0) 
        
        for y in hm1:
            if hm1[y] != hm2.get(y, 0):
                return False
            
        return True