class solution:
    
    def containsDuplicate(self, nums: list[int]) -> bool:
                            # Time:O(n)     Space:O(n)  SN: best Time 
        hash = set()       
        for n in nums:          #goes through the list one by one
            if n in hash:           #If n is in the set/hashmap return true
                return True     #If n is not in the set/hashmap then add it to the hash map 
            hash.add(n)        
        return False    
    
    
    
   
    def sneak(self, nums: list[int]) -> bool:
                                    # Time:?     Space:?  SN: best Space but 5% slower in time
        hash = set(nums)                #takes the list and puts it into a set/hashmap
        return len(nums) != len(hash)   
   
    
    print("\nContainsDuplicate:", containsDuplicate(None, [1,2,3,4]))
    print("sneak:", sneak(None, [1,2,3,4]))