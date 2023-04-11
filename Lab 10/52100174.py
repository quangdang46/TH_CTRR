T=['A',
'B','C',
None,'D','E','F',
None,None,'G','H',None,'I',None,None,
None,None,None,None,None,None,'J',None,None,None,'K','L',None,None,None,None]

class bNode(object):
  def __init__(self,data=None):
    self.left = None
    self.right = None
    self.data = data
  def breadthFirstSearch(root, data):
    if root is None:
        return None

    queue = []
    queue.append(root)

    while len(queue) != 0:
        curr = queue.pop(0)
        if curr.data == data:
            return curr
        if curr.left is not None:
            curr.left.parent = curr
            queue.append(curr.left)
        if curr.right is not None:
            curr.right.parent = curr
            queue.append(curr.right)

    return None
  
  def depthFirstSearch(root, data):
    if root is None:
        return None

    stack = []
    visited = set()
    stack.append(root)

    while len(stack) != 0:
        curr = stack.pop()
        visited.add(curr)
        if curr.data == data:
            path = []
            while curr is not None:
                path.append(curr.data)
                curr = curr.parent
            return path[::-1]
        if curr.left is not None and curr.left not in visited:
            curr.left.parent = curr
            stack.append(curr.left)
        if curr.right is not None and curr.right not in visited:
            curr.right.parent = curr
            stack.append(curr.right)

    return None
  
def breadthFirstSearchV(tree, data):
    if len(tree) == 0:
        return None, []

    queue = []
    queue.append((0, []))

    while len(queue) != 0:
        curr, path = queue.pop(0)
        if tree[curr] == data:
            return curr, path + [tree[curr]]
        if 2 * curr + 1 < len(tree) and tree[2 * curr + 1] is not None:
            queue.append((2 * curr + 1, path + [tree[curr]]))
        if 2 * curr + 2 < len(tree) and tree[2 * curr + 2] is not None:
            queue.append((2 * curr + 2, path + [tree[curr]]))

    return None, []
A=bNode('A')
A.left=bNode('B')
A.right=bNode('C')
B=A.left
C=A.right
B.right=bNode('D')
D=B.right
C.left=bNode('E')
C.right=bNode('F')
E=C.left
F=C.right
D.left=bNode('G')
D.right=bNode('H')
E.left=bNode('I')
G=D.left
H=D.right
I=E.left
H.left=bNode('J')
J=H.right
I.left=bNode('K')
I.right=bNode('L')
K=I.left
L=I.right

# 



# 3
def NLR(node):
    if node:
        print(node.data, end=' ')
        NLR(node.left)
        NLR(node.right)

def LNR(node):
    if node:
        LNR(node.left)
        print(node.data, end=' ')
        LNR(node.right)

def LRN(node):
    if node:
        LRN(node.left)
        LRN(node.right)
        print(node.data, end=' ')