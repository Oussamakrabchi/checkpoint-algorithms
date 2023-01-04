#!/usr/bin/env python
# coding: utf-8

# In[1]:


#test1
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))


# In[2]:


#test2
def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)

print(power(3,4))


# In[4]:


#test3
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [29,13,22,37,52,49,46,71,56]
bubbleSort(nlist)
print(nlist)


# In[5]:


#test4
def mergeSort(nlist):
    
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    

nlist = [29,13,22,37,52,49,46,71,56]
mergeSort(nlist)
print(nlist)


# In[15]:



#test5
def partition(array, low, high):
 

    pivot = array[high]
 
    
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
     
            i = i + 1
 
       
            (array[i], array[j]) = (array[j], array[i])
 

    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
  
    return i + 1
 

 
 
def quickSort(array, low, high):
    if low < high:
 
        
        pi = partition(array, low, high)
 
        
        quickSort(array, low, pi - 1)
 
      
        quickSort(array, pi + 1, high)
 
 
data = [29,13,22,37,52,49,46,71,56]

size = len(data)
 
quickSort(data, 0, size - 1)
 
print(data)


# In[ ]:





# In[ ]:




