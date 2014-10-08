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

def chop_tree(tree, start):
  """
  Chops extraneous nodes leaving only
  the starting node
  """
  tree = tree[start]
  return tree

def filter_tree(tree, end):
  """
  Removes ending nodes when they are not the
  last node of the branch.
  """
  if tree[end]:
    del tree[end]
  nodes = tree.keys()
  if len(nodes) > 1:
    for node in nodes:
      filter_tree(tree[node], end)
  return tree

def calculate_distance(tree, matrix, start, distance=0):
  """
  Adds up the distance from start to end
  """
  for node in tree:
    new_distance = distance + node_distance(matrix, start, node)
    if tree[node]:
      calculate_distance(tree[node], matrix, node, new_distance)
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
b = chop_tree(a, 'A')
c = filter_tree(b, 'G')
d = calculate_distance(c, x, 'A')
print(d)