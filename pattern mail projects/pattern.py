#!/usr/bin/env python
# coding: utf-8

# In[1]:


def A():
    for row in range(7):
        for col in range(5):
            if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
                print('*',end="")
            else:
                print(end=" ")
        
        print(end="")
        print() 


# In[2]:


def B():
    for row in range(7):
        for col in range(5):
            if (col==0) or (col==4 and(row!=0 and row!=3 and row!=6)) or ((col>0 and col<4) and (row==0 or row==3 or row==6)):
                print("*",end="")
            else:
                print(end=" ")
        print()  


# In[1]:


def C():
    #n=int(input('enter the number'))
    for row in range(4):
        for col in range(4):
            if (col==0 or (row==0 or row==4-1)):
                print('*',end="")
            else:
                print(end=" ")
        print()


# In[2]:


def D():
    for row in range(5):
        for col in range(4):
            if (col==0)  or (col==3 and (row!=0 and row!=4)) or((col>0 and col<3) and (row==0 or row==4)):
                print("*",end="")
            else:
                print(end=" ")
        print()


# In[4]:


def E():
    for row in range(7):
        for col in range(4):
            if (col==0) or (row==0 or row==3 or row==6):
                print("*",end="")
            else:
                print(end=" ")
        print()


# In[6]:


def F():
    for row in range(7):
        for col in range(4):
            if ((col==0) or (row==0 or row==3)):
                print("*",end="")
            else:
                print(end=" ")
        print()


# In[7]:


def G():
    for row in range(6):
        for col in range(4):
            if (col==0) or (row==0) or (col<2 and (row==5))or( col>1 and (row==4)):
                print("*",end="")
            else:
                print(end=" ")
        print()


# In[8]:


def H():
    for row in range(7):
        for col in range(5):
            if (col==0 or col==4) or (row==3):
                print('*',end="")
            else:
                print(end=" ")
        print()


# In[9]:


def I():
    for row in range(4):
        for col in range(3):
            if (col==1) or (row==0 or row==3):
                print('*',end="")
            else:
                print(end=" ")
        print()


# In[10]:


def J():
    for row in range(4):
        for col in range(3):
            if (col==1) or (row==0)or (row==3 and col<2):
                print('*',end="")
            else:
                print(end=" ")
        print()


# In[12]:


def K():
    i=0
    j=4
    for row in range(7):
        for col in range(5):
            if (col==0) or (row==col+2 and col>1):
                 print('*',end="")
            elif (row==i and col==j) and col>0:
                print('*',end="")
                i=i+1
                j=j-1
            else:
                print(end=" ")
        print()


# In[13]:


def L():
    for row in range(5):
        for col in range(4):
            if (col==0 or row==4):
                print('*',end="")
            else:
                print(end=" ")
        print()
        


# In[14]:


def M():
    for row in range(7):
        for col in range(7):
            if (col==0 or col==6) or((row==col) and row<4) or ((row+col==6) and row<3):
                    print('*',end="")
            else:
                print(end=" ")
        print()
   


# In[15]:


def N():
    for row in range(7):
        for col in range(7):
            if (col==0 or col==6) or(row==col) :
                    print('*',end="")
            else:
                print(end=" ")
        print()


# In[16]:


def O():
    for row in range(5):
        for col in range(5):
            if ((col==0 or col==4) and (row>0 and row<4)) or ((row==0 or row==4) and (col<4 and col>0)):
                print('*',end="")
            else:
                print(end=" ")
        print()


# In[17]:


def P():
    
    for row in range(5):
        for col in range(5):
            if (col==0 ) or ((row==0 or row==2) or (col==4 and row<3)): #or (row-col==2) :
                print("*",end="")
            else:
                print(end=" ")
        print()


# In[18]:


def Q():
    for row in range(6):
        for col in range(5):
            if ((col==0 or col==4) and (row>0 and row<4)) or ((row==0 or row==4) and (col<4 and col>0)) or(col==4 or row==5):
                print('*',end="")
            else:
                print(end=" ")
        print()


# In[20]:


def R():
    for row in range(6):
        for col in range(5):
            if (col==0 ) or ((row==0 or row==2) or (col==4 and row<3)) or (row-col==2) :
                print("*",end="")
          
            else:
                print(end=" ")
        print()


# In[21]:


def S():
    for row in range(7):
        for col in range(5):
            if ((col>0 and col<4) and (row==0 or row==3 or row==6)) or (col==0 and (row>0 and row<3))or (col==4 and (row>3 and row<6)):
                       print("*",end="")
          
            else:
                print(end=" ")
        print()
                


# In[23]:


def T():
    for row in range(4):
        for col in range(3):
            if (col==1) or (row==0 ):
                print('*',end="")
            else:
                print(end=" ")
        print()


# In[24]:


def U():
    for row in range(5):
        for col in range(5):
            if ((col==0 or col==4) or row==4):
                print("*",end="")
          
            else:
                print(end=" ")
        print()


# In[25]:


def V():
    for row in range(4):
        for col in range(7):
            if (row==col) or (row+col==6):
                print("*",end="")
          
            else:
                print(end=" ")
        print()


# In[26]:


def W():
    for row in range(4):
        for col in range(7):
            if ((col==0 or col==6) or (row+col==3)) or ((col>3 and col<5) and (row+col==5)) :
                print("*",end="")
          #  elif (row==i and col==j):
           #     print('*',end="")
           #     i=i+1
           #     j=j-1
                
            else:
                print(end=" ")
        print()


# In[27]:


def X():
    for row in range(4):
        for col in range(7):
            if (row==col) or (row+col==3):
                print("*",end="")
          
            else:
                print(end=" ")
        print()


# In[28]:


def Y():
    for row in range(5):
        for col in range(5):
            if (col==2 and row>1) or (row==col and col<2) or (row==0 and col==4) or(row==1 and col==3):
                print("*",end="")
          
            else:
                print(end=" ")
        print()


# In[29]:


def Z():
    for row in range(5):
        for col in range(5):
            if (row==0 or row==4) or (row+col==4):
                print("*",end="")
          
            else:
                print(end=" ")
        print()


# In[ ]:




