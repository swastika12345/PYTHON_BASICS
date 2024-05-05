#TREE

class bstnode:
  def __init__(self,val=None):
    self.left=None
    self.right=None
    self.val=val
def insert(self,val):
  if not self.val:
    self.val=val
    return
  if self.val==val:
    return
  if val<self.val:
    if self.left:
      self.left.insert(val)
      return
    self.left=bstnode(val)
    return
  if self.right:
    self.right.insert(val)
    return
  self.right=bstnode(val)
def get_min(self):
  current=self
  while current.left is not None:
    current=current.left
  return current.val
def get_max(self):
  current=self
  while current.right is not None:
    current=current.right
  return current.val  
def delete(self,val):
  if self== None:
    return self
  if val < self.val:
    self.left=self.left.delete(val)
    return self
  if val > self.val:
    self.right=self.right.delete(val)
    return self
  if self.right == None:
    return self.left
  if self.left == None:
    return self.right
  min_larger_node = self.right
  while min_larger_node.left:
    min_larger_node = min.larger.node.left
  self.val = min_larger_node.left 
  self.right = self.right.delete(min_larger_node.val)
  return self
def inorder(self, val):
    if self.left is not None:
        self.left.inorder(val)
    if self.val is not None:
        val.append(self.val)
    if self.right is not None:
        self.right.inorder(val)
    return val
def preorder(self, val):
    if self.val is not None:
        val.append(self.val)
    if self.left is not None:
        self.left.preorder(val)
    if self.right is not None:
        self.right.preorder(val)
    return val
def postorder(self, val):
    if self.left is not None:
        self.left.postorder(val)
    if self.right is not None:
        self.right.postorder(val)
    if self.val is not None:
        val.append(self.val)
    return val
def exists(self, val):
    if val == self.val:
        return True
    if val < self.val:
        if self.left == None:
            return False
        return self.left.exists(val)
    if self.right == None:
        return False
    return self.right.exists(val)    
#driver code
    r = node(50)
    r=insert(self,20)
    r=insert(self,30)
    r=insert(self,10)
    r=insert(self,40)
    r=insert(self,50)
    r=insert(self,60)
    r=insert(self,80)
    print("Inorder:")
    inorder(r)                          