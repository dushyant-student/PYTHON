# class Solution():
#     def longestCommonPrefix(self, strs):
#         self.strs=strs
#         self.len=len(strs)
#         self.lst=[]
#         for i in range(0,self.len):
#             if self.strs==[]:
#                 print('""')
#                 break
#             elif self.strs[0][i]==self.strs[1][i] and self.strs[1][i]  == self.strs[2][i] and self.strs[2][i]  == self.strs[2][i]:
#                 (self.lst).append(self.strs[0][i])
#             else:
#                 return ('"'+("".join(self.lst)+'"'))
#                 break
# strs=["flower","flow","flight"]
# obj=Solution() 
# val=obj.longestCommonPrefix(strs)
# print(val)



#print("He said, \"Hello!\"")




# for j in range(0,5):
#     print(str(j).strip())

# l="''"
# l=l+"P"
# print(l)



class Solution(object):
    def mergeTwoLists(self, list1, list2):
        self.list1=list1
        self.list2=list2
        self.list3=self.list1+self.list2
        self.list3.sort()
        return (self.list3)
list1=[0,2,4]
list2=[1,3,4]
obj=Solution()
ans=obj.mergeTwoLists(list1, list2)
print(ans)
        
        
        
        
# l=[1, 2, 4, 1, 3, 4]
# l.sort()
# print(l)