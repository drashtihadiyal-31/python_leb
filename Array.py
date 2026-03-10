# Integer array 
"""from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr)) """


# Basic Array Operations:

""" 
1. len() = number of elements 
from array import array
arr=array('i',[10,20,30,40,50])
print(len(arr)) 

2. append(x) = add element at end             
from array import array
arr=array('i',[10,20,30,40])
arr.append(40)
print(arr) 

3. insert(pos,x) = insert at position
from array import array
arr=array('i',[10,20,30])
arr.insert(2,40)
print(arr)

4. remove(x) = remove first occurence
from array import array
arr=array('i',[10,20,30])
arr.remove(20)
print(arr) 

5. pop() = remove and return last element 
from array import array
arr=array('i',[10,20,30,40])
x = arr.pop()
print ("remove : " , x )
print(arr) 

6. index(x) = find index of element 
from array import array
arr = array('i',[10,20,30,40])
print(arr.index(30)) 

7. count(x) = count occurence 
from array import array
arr = array('i',[10,20,30,20,40])
print(arr.index(20)) 

8. reverse() = reverse array 
from array import array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)"""


#indexing array:

"""
1. positive indexing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])

2. negative indexing
arr=array('i',[10,20,30,40,50])
print(arr[-1])
print(arr[-2])
print(arr[-5])

3. modifying elements using index
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)

4. index error
arr=array('i',[10,20,30])
print(arr[5])"""


# Slicing in Array :

""" 1. Basic slices 
from array import array
arr = array('i',[10,20,30,40,50])
print(arr[1:4]) # index 1 to 3
print(arr[:3]) # start to index 2
print(arr[2:]) # index 2 to end
print(arr[:]) # entire array 

2. Slicing with step 
from array import array
arr = array('i',[10,20,30,40,50,60,70,80])
print(arr[::2]) # every second elements
print(arr[::3]) # every third elements
print(arr[1::2]) # every second element starting from index 1

3. Negative slicing 
from array import array
arr = array('i',[10,20,30,40,50])
print(arr[-4:-1]) # from index -4 to -2
print(arr[-3:]) # last third elements
print(arr[:-2]) # all except last two

4. Reverse array using slicing 
from array import array
arr = array('i',[10,20,30,40,50])
print(arr[::-1]) 

5. Modifying slices
from array import array
arr = array('i',[10,20,30,40,50])
arr[1:4] = array('i',[25,35,45])
print(arr) """
