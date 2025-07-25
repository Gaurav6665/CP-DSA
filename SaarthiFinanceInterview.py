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




