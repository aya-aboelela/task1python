#!/usr/bin/env python
# coding: utf-8

# In[6]:


import networkx as nx
F = nx.Graph()
nodes = ['a','b', 'c', 'd']
F.add_nodes_from(nodes)
edges = [('a','b'),('a', 'c'), ('b', 'c'), ('c', 'd'),('a','d'),('b','d')]
F.add_edges_from(edges)
nx.draw(F, with_labels=True,node_color='#5D4E6D',
        node_size=1600,
        font_color='white',
        font_size=16,)


# In[8]:


F.nodes()


# In[9]:


for node in F.nodes:
    print(node)


# In[10]:


F.number_of_nodes()


# In[11]:


F.number_of_edges()


# In[12]:


F.neighbors('b')


# In[13]:


for neighbor in F.neighbors('b'):
    print(neighbor)


# In[14]:


list(F.neighbors('b'))


# In[15]:


nx.is_tree(F)


# In[16]:


nx.is_connected(F)


# In[17]:


F.has_node('d')


# In[18]:


for edge in F.edges:
    print(edge)


# In[19]:


F.edges()


# In[20]:


'd' in F.nodes


# In[21]:


F.has_edge('a', 'c')


# In[22]:


('c', 'd') in F.edges


# In[23]:


len(list(F.neighbors('c')))


# In[24]:


F.degree('d')


# In[26]:


#Solve Of EXERCISE 1
import networkx as nx
F = nx.Graph()
nodes = ['a','b', 'c']
F.add_nodes_from(nodes)
edges = [ ('a', 'b'),('a', 'd'),('c', 'd'),]
F.add_edges_from(edges)
nx.draw(F, with_labels=True,node_color='#ae2012',
        node_size=1600,
        font_color='white',
        font_size=16,)


# In[27]:


def get_leaves(F):
    li=[]
    for j in F.nodes():
        if F.degree(j)==1:
            li.append(j)
    return li


# In[28]:


get_leaves(F)


# In[29]:


#Solve Of Exercise 2
print(open('friends.adjlist').read())


# In[30]:


SF = nx.read_adjlist('friends.adjlist')


# In[39]:


nx.draw(SF, node_size=2000, node_color='#333d29', with_labels=True,font_color='white')


# In[ ]:




