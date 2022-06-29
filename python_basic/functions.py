
#lambda expression

# filter

# mylist = [1,2,3,4,5,6,7,8]
# filtered=[]
# def even_bool(a):
#      for num in a:
#
#           if num%2 == 0:
#                filtered.append(num)
#           print(filtered)
#
# print(even_bool(mylist))

mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
     return num%2 == 0

evens = filter(even_bool,mylist)
print(list(evens))