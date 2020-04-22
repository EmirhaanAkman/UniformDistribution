#!/usr/bin/env python
# coding: utf-8

# In[7]:


""""
EMİRHAN AKMAN 180401068
Github: https://github.com/EmirhaanAkman/Programlama-Lab
"""


# In[8]:




import sympy as sym
from sympy import Symbol, pprint, Piecewise
import sympy.plotting as syp
import matplotlib.pyplot as plt

a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
ud = 1 /(b-a)


# In[9]:


pprint(ud)


# In[14]:


#id = int(input('Ilk degeri giriniz'))
#sd= int(inpıt('Son degeri giriniz'))
def uniformDis(id, sd):
    syp.plot(Piecewise((0, (x < id) | (x > sd)), (ud.subs({a: id, b: sd}), (x >= id) & 
        (x <= sd))), (x, -15, 15), title="uniformDistribution")


# In[15]:


uniformDis(3,10)


# In[16]:


from numpy import random
import seaborn as sns
sns.distplot(random.uniform(size=1000), hist=False)

plt.show()

