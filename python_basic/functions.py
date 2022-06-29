
#
# def arrayCheck(nums):
#
#      for i in range(len(nums)-2):
#           if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
#                return True
#      return False
#
#
# print(arrayCheck([1,2,4,1,2,3]))

# def stringBits(mystring):
#      result = ""
#
#      for i in range(len(mystring)):
#           if i%2 ==0:
#                result = result + mystring[i]
#      return result
#
# mystring = 'HeeoLoLeo'
# print(stringBits(mystring))


def count_evens(nums):
     count = 0

     for element in nums:
          if element % 2 == 0:
               count +=1
     return count


print(count_evens([1,2,3,4,5,6]))