class solution: 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #empty hash to put value and index
        hash = {} #val : index 
        
        #iterates through array
        for x, y in enumerate(nums):
            
            #Calculates the difference between the int and the target 
            difference = target - y
            
            if difference in hash:
                return [hash[difference], x]
            hash[y] = x
            
            
        #return 
        
