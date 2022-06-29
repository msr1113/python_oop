mylist = [1,2,3,4,5,6,7,8]
filtered=[]
def even_bool(a):
     for num in range(len(a)):

          if num%2 == 0:
               filtered.append(num)
     return filtered

print(even_bool(mylist))