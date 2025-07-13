# class Solution():
#     def addTwoNumbers(self, l1, l2):
#         self.l1=l1
#         self.l2=l2
#         self.n1=""
#         for i in range(len(l1)-1,-1,-1):
#             self.n1=str(self.n1)+str(self.l1[i])
#         print(self.n1)
#         self.n2=""
#         for i in range(len(l2)-1,-1,-1):
#             self.n2=str(self.n2)+str(self.l2[i])
#         print(self.n2)
#         self.lst=[]
#         self.new_val=int(self.n1)+int(self.n2)
#         self.stp=str(self.new_val)
#         for j in range(len(self.stp)-1,-1,-1):
#             self.lst.append(self.stp[j])
#         print(self.lst)

# l1=[2,4,3]
# l2=[5,6,4]
# obj=Solution()
# result=obj.addTwoNumbers(l1,l2)
# print(result)





# class Solution():
#     def findMedianSortedArrays(self, nums1, nums2):
#         self.nums1=nums1
#         self.nums2=nums2
#         self.new_arr=(self.nums1+self.nums2)
#         i=0
#         for j in self.new_arr:
#             i=i+j
#         self.ans=i/len(self.new_arr)
#         return self.ans
# nums1=[1,2]
# nums2=[3,4]
# obj=Solution()
# res=obj.findMedianSortedArrays(nums1,nums2)
# print(res)



# arr=["mynam","hdvdgs","wasre"]
# print(arr[0][1])