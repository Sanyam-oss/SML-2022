#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm


# In[35]:


x = np.linspace(-1,8,1000)

pw1 = 1/4
pw2 = 3/4

pxw1 = norm.pdf(x,2,1)
pxw2 = norm.pdf(x,5,1)

# px = (pxw1*pw1) + (pxw2*pw2)

pw1x = (pxw1*pw1)
pw2x = (pxw2*pw2)


# In[45]:


plt.plot(x,pxw1,'b',label = 'P(x/w1)')
plt.xlabel("x")
plt.ylabel("P(x/w1)")
plt.legend()
plt.show()


# In[46]:


plt.plot(x,pxw2,'r',label = 'P(x/w2)')
plt.xlabel("x")
plt.ylabel("P(x/w2)")
plt.legend()
plt.show()


# In[51]:


x_axis = np.linspace(0,8,1000)

new_pdf = norm.pdf(x_axis,2,1)/norm.pdf(x_axis,5,1)

plt.plot(x_axis,new_pdf,'c',label="P(x/w1)/P(x/w2)")

plt.xlabel("x")
plt.ylabel("P(x/w1)/P(x/w2)")
plt.legend()

plt.show()


# In[52]:


# Decision boundary (Zero-one loss)

plt.plot(x,pw1x,'b',label = 'P(w1/x)')
plt.plot(x,pw2x,'r',label = 'P(w2/x)')

plt.axvline(x=3.137)

plt.xlabel("x")
plt.ylabel("P(wi/x)")
plt.legend()
plt.show()


# In[59]:


# Decision boundary (Acc to given loss fxn)

plt.plot(x,3*pw1x,'b',label = 'R(alpha1/x)')
plt.plot(x,2*pw2x,'r',label = 'R(alpha2/x)')

plt.axvline(x=3.137,linestyle='--')
plt.axvline(x=3.268)

plt.xlabel("x")
plt.ylabel("r(alphai/x)")
plt.legend()
plt.show()


# In[ ]:




