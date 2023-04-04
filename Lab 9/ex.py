import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

A1=np.array([[0,3,5,2],
 [0,0,2,0],
 [0,0,0,3],
 [0,0,0,0]])
G1 = nx.DiGraph(np.array(A1))
pos=nx.spring_layout(G1)
nx.draw_networkx(G1,pos=pos,with_labels=True,labels={a:b for a,b in enumerate('abcd')})
edge_labels = nx.draw_networkx_edge_labels(G1,font_size=6,pos=pos,label_pos=0.5)
plt.axis('equal')
plt.show()


def mPlus(A,B):
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j]+=B[i][j]
  return A
  

def mMinus(A,B):
    # return A-B
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j]-=B[i][j]
    return A

def mMultiply(A,B):
    # return A@B
    C=np.zeros((len(A),len(B[0])))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j]+=A[i][k]*B[k][j]
    return C


def mTranspose(A):
    # return A.T
    B=np.zeros((len(A[0]),len(A)))
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i]=A[i][j]
    return B


A=[
    ['A','C',5],
    ['A','D',3],
    ['B','C',3],
    ['B','D',2],
    ['C','D',1],
    ['C','E',3],
  ['D','E',1],
  ['D','F',3],
  ['E','F',4],
]

def weightedMatrix(edges):
    nodes=[]
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])
    nodes.sort()
    # print(nodes)
    A=np.zeros((len(nodes),len(nodes)))
    for edge in edges:
        A[nodes.index(edge[0])][nodes.index(edge[1])]=edge[2]
    return A,nodes

print('a)')
A,nodes=weightedMatrix(A)
print(A)



def toLoE(A):
    edges=[]
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i][j]!=0:
                edges.append([i,j,A[i][j]])
    return edges


B=[
    ['Monkeys','Primates'],
    ['Apes','Primates'],
    ['Gorillas','Primates'],
    ['Mice','Rodents'],
    ['Squirrels','Rodents'],
    ['Beavers','Rodents'],
    ['Crocodiles','Reptiles'],
    ['Komodo dragons','Reptiles'],
    ['Lizards','Reptiles'],
    ['Coconut trees','Plants'],
    ['Grasses','Plants'],
    ['Oaks','Plants'],
    ['Mushrooms','Fungi'],
    ['Molds','Fungi'],
    ['Yeasts','Fungi'],
    ['Primates','Mammals'],
    ['Rodents','Mammals'],
    ['Mammals','Animals'],
    ['Rodents','Animals'],
    ['Reptiles','Animals'],
    ['Animals','Multicellular organisms'],
    ['Plants','Multicellular organisms'],
    ['Mushrooms','Multicellular organisms'],
    ['Molds','Multicellular organisms'],
    ['Yeasts','Unicellular organisms'],
]


G = nx.DiGraph()

nodes = set([item for sublist in B for item in sublist])
for node in nodes:
    G.add_node(node)

for edge in B:
    G.add_edge(edge[0], edge[1])

colors = []
for node in nodes:
    if node in ['Monkeys', 'Apes', 'Gorillas']:
        colors.append('blue')
    elif node in ['Mice', 'Squirrels', 'Beavers']:
        colors.append('orange')
    elif node in ['Crocodiles', 'Komodo dragons', 'Lizards']:
        colors.append('green')
    elif node in ['Coconut trees', 'Grasses', 'Oaks']:
        colors.append('brown')
    elif node in ['Mushrooms', 'Molds', 'Yeasts']:
        colors.append('purple')

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, with_labels=True, node_color=colors)
edge_labels = nx.draw_networkx_edge_labels(G, pos=pos, font_size=8, edge_labels={(edge[0], edge[1]): edge[1] for edge in B})
plt.axis('equal')
plt.show()