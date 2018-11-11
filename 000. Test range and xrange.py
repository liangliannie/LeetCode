import sys 
  
# initializing a with range() 
a = range(1,10) 
  
# initializing a with xrange() 
x = xrange(10,20) 
  
# testing the size of a 
# range() takes more memory 
print ("The size allotted using range() is : ") 
print (sys.getsizeof(a)) 
  
# testing the size of a 
# range() takes less memory 
print ("The size allotted using xrange() is : ") 
print (sys.getsizeof(x)) 

# testing usage of slice operation on range() 
# prints without error 
print ("The list after slicing using range is : ") 
# print (a[2:5]) 
  
# testing usage of slice operation on xrange() 
# raises error 
print ("The list after slicing using xrange is : ") 
# print (x[2:5]) 
for i in a:
    print(i)

for i in x:
    print(i)