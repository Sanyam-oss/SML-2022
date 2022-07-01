#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
from scipy.stats import cauchy


# In[27]:


x = np.linspace(-1,8,1000)

pw1 = pw2 = 1/2    # Assumption

pxw1 = cauchy.pdf(x,3,1)
pxw2 = cauchy.pdf(x,5,1)

px = (pxw1*pw1) + (pxw2*pw2)

pw1x = pxw1*pw1/px
pw2x = pxw2*pw2/px


# In[28]:


plt.plot(x,pw1x,'r',label = 'p(w1/x)')
plt.plot(x,pw2x,'b',label = 'p(w2/x)')

plt.xlabel("x")
plt.ylabel("P(wi/x)")
plt.legend()
plt.show()


# In[29]:


# DECISION BOUNDARY

plt.plot(x,pw1x,'r',label = 'p(w1/x)')
plt.plot(x,pw2x,'b',label = 'p(w2/x)')

plt.axvline(x = 4)

plt.xlabel("x")
plt.ylabel("P(wi/x)")
plt.legend()
plt.show()


# In[ ]:




