#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python program to find sum of elements in list?

# In[7]:


l1=[]
sum=0
n=int(input('enter the number of element '))
for i in range(n):
    ele=float(input('enter the elements '))
    l1.append(ele)
print(l1)
for i in range(n):
    sum =sum+l1[i]
print('the sum of all elements are: ',sum)

    


# # 2. Write a Python program to Multiply all numbers in the list?

# In[8]:


l2=[]
m=1
n=int(input('enter the number of element '))
for i in range(n):
    ele=float(input('enter the elements '))
    l2.append(ele)
print(l2)
for i in range(n):
    m=m*l2[i]
print('the multiplication of all number is: ',m)


# # 3. Write a Python program to find smallest number in a list?

# In[9]:


l3=[]
n=int(input('enter the number of element '))
for i in range(n):
    ele=float(input('enter the elements '))
    l3.append(ele)
print(l3)
print('the smallest number in list : ',min(l3))

        


# # 4. Write a Python program to find largest number in a list?

# In[6]:


l4=[]
n=int(input('enter the number of element '))
for i in range(n):
    ele=float(input('enter the elements '))
    l4.append(ele)
print(l4)
print('the largest number in list : ',max(l4))


# # 5. Write a Python program to find second largest number in a list?
# 

# In[18]:


l5=[]
n=int(input('enter the number of element '))
for i in range(n):
    ele=float(input('enter the elements '))
    l5.append(ele)
print(l5)
l5.sort()
print(' second largest number in a list: ',l5[n-2])




        


# # 6. Write a Python program to find N largest elements from a list?

# In[5]:


l6=[]
n=int(input('enter the number of element '))
for i in range(n):
    ele=float(input('enter the elements '))
    l6.append(ele)
l6.sort(reverse=True)
N=int(input('enter how many largest elements you want to print in list: '))
print(l6[:N])


# # 7. Write a Python program to print even numbers in a list?

# In[3]:


l7=[]
n=int(input('enter the number of element '))
for i in range(n):
    ele=float(input('enter the elements '))
    l7.append(ele)
for i in l7:
    if i%2==0:
        print(i)
    


# # 8. Write a Python program to print odd numbers in a List?

# In[2]:


l8=[]
n=int(input('enter the number of element '))
for i in range(n):
    ele=float(input('enter the elements '))
    l8.append(ele)
for i in l8:
    if ((i%2)!=0):
        print(i)
    


# # 9. Write a Python program to Remove empty List from List?

# In[15]:


l9=[4,5,[],76,[4,5,6],[]]
l9=[i for i in l9 if i!=[]]
print(l9)
    


# # 10. Write a Python program to Cloning or Copying a list?

# In[19]:


import copy
l10=[4,5,6,7]
l11=copy.copy(l10)
print(l11)


# # 11. Write a Python program to Count occurrences of an element in a list?

# In[1]:


l12=[]
n=int(input('enter the number of element '))
for i in range(n):
    ele=float(input('enter the elements '))
    l12.append(ele)
m=float(input('enter the number to check occurrences '))
count=l12.count(m)
print(f'the number occur {count} times')


# In[ ]:




