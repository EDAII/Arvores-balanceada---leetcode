# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class T:
  isBST: bool | None = False
  mx: int | None = None
  mn: int | None = None
  summ: int | None = None

class T:
    def __init__(self, isBST=False, mx=None, mn=None, summ=None):
        self.isBST = isBST
        self.mx = mx
        self.mn = mn
        self.summ = summ


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def traverse(root: Optional[TreeNode]) -> T:
          
            if not root:
                return T(True, -math.inf, math.inf, 0)

 
            left: T = traverse(root.left)
            right: T = traverse(root.right)

        
            if left.isBST and right.isBST and \
               root.val > left.mx and root.val < right.mn:
                
              
                current_summ = root.val + left.summ + right.summ
                
                
                self.ans = max(self.ans, current_summ)
                
              
                return T(True, 
                         max(root.val, right.mx), 
                         min(root.val, left.mn),  
                         current_summ)

            else:
                return T(False)

       
        traverse(root)
        
        return self.ans