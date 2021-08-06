# Link: https://www.hackerrank.com/challenges/is-binary-search-tree/problem
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""



def descend(root, limits):
    if root == None:
        return True
    if limits[0] is not None and root.data >= limits[0]:
        return False
    if limits[1] is not None and root.data <= limits[1]:
        return False
    return (descend(root.left, (root.data, limits[1])) 
        and descend(root.right, (limits[0], root.data)) )
        
def check_binary_search_tree_(root):
    return descend(root, (None, None))