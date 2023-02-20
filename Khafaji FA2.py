#!/usr/bin/env python
# coding: utf-8

# In[8]:


def multiplyList():
    product = 1
    numList = [1,2,3,4,5,6,7,8,9,-10,2,78]
    for x in numList:
        product *= x
    
    print(product)

multiplyList()


# In[41]:


def boxBox():
    vert=0
    while vert<21:
        horiz = 0 
        # if vert-1%5 = 0  then may characters, if wala puro space lang
        while horiz<21:
            if vert%5 == 0:
                if horiz%5 == 0:
                    if horiz<20:
                        print("\N{ghost}", end=" ")
                        horiz+=1
                    else:
                        print("\N{ghost}")
                        horiz+=1
                elif horiz:
                    print("\N{skull and crossbones}", end=" ")
                    horiz+=1
            else:
                if horiz%5 == 0:
                    if horiz<20:
                        print("\N{spider web}", end=" ")
                        horiz+=1
                    else:
                        print("\N{spider web}")
                        horiz+=1
                else:
                    print("  ", end=" ")
                    horiz+=1
        vert+=1
        
        #yung print corner, then if horiz<5 print smth 4 times (loop)

boxBox()


# In[ ]:





# In[ ]:




