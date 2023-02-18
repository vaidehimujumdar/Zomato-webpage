visited = [] # List for visited nodes.
queue = [] #Initialize a queue
def bfs(visited, graph, node): #function for BFS
  visited.append(node)
queue.append(node)
while queue: # Creating loop to visit each node
  m = queue.pop(0)
print (m, end = "\n")
for neighbour in [m]:
  if neighbour not in visited:
   visited.append(neighbour)
queue.append(neighbour)