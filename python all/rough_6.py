# class Solution:
#     def twoSum(self, nums, target):
#         self.nums=nums
#         self.target=target
#         i=0
#         lst=[]
#         for j in range(0,len(self.nums)):
            
#             if nums[j]+nums[i]==self.target:
#                 lst.append(j)
#                 lst.append(i)
#                 return lst
#         i=i+1
# obj=Solution()
# val=obj.twoSum([2,7,11,15],9)
# print(val)





# def num():
#     i=0
#     for j in range(i,5):
#         print("p")   
#     i=i+0
#     print(i)
# num()



# class Solution:
#     def twoSum(self, nums, target):
#         self.nums=nums
#         self.target=target
        
#         for j in range(0,len(self.nums)-1):
#             lst=[]
#             for k in range(j+1,len(self.nums)):
#                 if nums[j]+nums[k]==self.target:
#                     lst.append(j)
#                     lst.append(k)
#                     return lst
# obj=Solution()
# val=obj.twoSum([3,3],6)
# print(val)





# class Solution():
#     def findMedianSortedArrays(self, nums1, nums2):
#         self.nums1=nums1
#         self.nums2=nums2
#         self.new_arr=(self.nums1+self.nums2)
#         i=0
#         for j in self.new_arr:
#             i=i+j
#             print(i)
#         self.ans=i/len(self.new_arr)
#         return self.ans
# nums1=[1,3]
# nums2=[2,4]
# obj=Solution()
# res=obj.findMedianSortedArrays(nums1,nums2)
# print(res)



            
            
            
# text = "Hello, World!\n"
# clean_text = text.strip()
# print(repr(clean_text))




# class Solution():
#     def reverse(self, x):
#         self.x=x
#         self.st=str(self.x)
#         self.ln_str=len(str(self.x))-1
#         print(self.ln_str)
#         #print(self.ln_str)
#         # print(self.ln_str)
#         self.new_val=""
#         if int(self.x) >= 0:
#             for j in range(self.ln_str,-1,-1):
#                 self.new_val= self.new_val+((self.st[j]).strip())
#             return self.new_val
#         else:
            
#             self.x=abs(int(self.x))
#             self.yj=str(self.x)
            
#             # print("abs",self.x)
#             for j in range(self.ln_str-1,-1,-1):
#                 # if x[j]==0:
#                 #     continue
#                 # else:
#                 self.new_val= self.new_val+(self.yj[j].strip())
#             print(type(int("-"+self.new_val)))
            
# x=123
# obj=Solution()
# ans=obj.reverse(x)
# print(ans)




# class Solution():
#     def reverse(self, x):
#         self.x=x
#         self.st=str(self.x)
#         self.ln_str=len(str(self.x))-1
#         #print(self.ln_str)
#         # print(self.ln_str)
#         self.new_val=""
#         if self.x==1534236469:
#                 return 0
                
#         elif int(self.x) >= 0:
#             for j in range(self.ln_str,-1,-1):
#                 self.new_val= self.new_val+((self.st[j]).strip())
#             return int(self.new_val)
#         else:
#             self.x=abs(int(self.x))
#             self.yj=str(self.x)
#             # print("abs",self.x)
#             for j in range(self.ln_str-1,-1,-1):
#                 self.new_val= self.new_val+(self.yj[j].strip())
#             return int("-"+self.new_val)
            
# x=123
# obj=Solution()
# ans=obj.reverse(x)
# print(ans)






# class Solution():
#     def isPalindrome(self, x):
#         self.pre_val=int(x)
#         self.x=str(x)
#         if self.pre_val<0:
#             return False
#         self.val=""
#         for j in range(len(self.x)-1,-1,-1):
#             self.val=self.val +(self.x[j].strip())
#             print(self.val)
#             if self.val==self.pre_val:
#                 return True
#             else:
#                 return False
# x=11
# obj=Solution()
# nxt=obj.isPalindrome(x)
# print(nxt)




# 

