x = {
  'A': {
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 1,
    'F': 1,
    'G': 1,
  },  
  'B': {
    'A': 1,
    'C': 1,
    'D': 1,
    'E': 1,
    'F': 1,
    'G': 1,
  },
  'C': {
    'B': 1,
    'A': 1,
    'D': 1,
    'E': 1,
    'F': 1,
    'G': 1,
  },
  'D': {
    'B': 1,
    'C': 1,
    'A': 1,
    'E': 1,
    'F': 1,
    'G': 1,
  },
  'E': {
    'B': 1,
    'C': 1,
    'D': 1,
    'A': 1,
    'F': 1,
    'G': 1,
  },
  'F': {
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 1,
    'A': 1,
    'G': 1,
  },
  'G': {
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 1,
    'F': 1,
    'A': 1,
  },
}

def matrix_to_tree(nodes):
  """
  Creates a tree of all possible combinations of
  provided nodes in dict format
  """
  tree = {}
  for node in nodes:
    children = nodes[:]
    children.remove(node)
    tree[node] = matrix_to_tree(children)
  return tree

def set_start(tree, start):
  """
  Removes extraneous starting nodes if only one
  starting location is desired.
  """
  tree = tree[start]
  return tree

def set_end(tree, end):
  """
  Removes ending nodes when they are not the
  last node of the branch.  Used when one
  ending location is desired.
  """
  if tree[end]:
    del tree[end]
  nodes = tree.keys()
  if len(nodes) > 1:
    for node in nodes:
      set_end(tree[node], end)
  return tree

def map_distance(tree, matrix, start, distance=0):
  """
  Adds up the distance from start to end
  """
  for node in tree:
    new_distance = distance + node_distance(matrix, start, node)
    if tree[node]:
      map_distance(tree[node], matrix, node, new_distance)
    else:
      tree[node] = new_distance
  return tree

def node_distance(matrix, start, end):
  """
  Searches a matrix for the value
  of two points
  """
  return matrix[start][end]

nodes = [key for key in x.keys()]
a = matrix_to_tree(nodes)
b = set_start(a, 'A')
c = set_end(b, 'G')
d = map_distance(c, x, 'A')
print(d)