#saarathi Finance , Pranshu Sharma

class Node:
	def __init__(self,value):
		self.val = val
		self.p1 = None
		self.p2= None
A.p1 = B
B.p2 = C
C.p2 = D
D.p2= E

B.p1 = F
F.p1 = K

c.p1 = G
G.p2 = H
H.p2 = I

E.p1 = J
J.p1 = L
L.p2 = M

 #traverse DFS
def dfs(node):
    if not node:
          return
    print(node.val, end=' ')
   dfs(node.p1)
   dfs(node.p2)

dfs(A)


#Interactive version he asked on whatsapp to sent-
#used stack instead recurtion as that does stack overflow-

class Node:
    def __init__(self, val):
        self.val = val
        self.p1 = None
        self.p2 = None

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
J = Node('J')
K = Node('K')
L = Node('L')
M = Node('M')

A.p1 = B
B.p2 = C
C.p2 = D
D.p2 = E

B.p1 = F
F.p1 = K
C.p1 = G
G.p2 = H
H.p2 = I

E.p1 = J
J.p1 = L
L.p2 = M

def dfs(root):
    if not root:
        return []

    stack = []
    visited = set()
    result = []

    stack.append(root)

    while stack:
        node = stack[-1]

        if node in visited:
            stack.pop()
            result.append(node.val)
            continue

        visited.add(node)

        # Push children only if not visited
        if node.p2 and node.p2 not in visited:
            stack.append(node.p2)
        if node.p1 and node.p1 not in visited:
            stack.append(node.p1)

    return result

output = dfs(A)

print("DFS Post-order traversal:", output)

#Used a stack to simulate the call stack and a visited set to ensure each node is processed only after its children.

#This approach avoids stack overflow which could be case in recursion wala approach, handles large trees.
#By pushing the sibling (p2) before the child (p1), the stack ensures we process all children before visiting the parent.
	


