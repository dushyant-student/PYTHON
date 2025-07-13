class Solution():
    def removeDuplicates(self, nums):
        self.new_arr=[]
        self.val=0
        for k in nums:
            if k not in self.new_arr:
                self.new_arr.append(k)
        for f in range(0,len(self.new_arr)): 
            self.char=nums.count(self.new_arr[f])
            
            if self.char>=2:
                self.val=self.val+((self.char)-1)
        for h in range(1,self.val+1):    
            self.new_arr.append("_")
        return self.my
                
nums=[1,1,2]
obj=Solution()
ans=obj.removeDuplicates(nums)
print(ans)

