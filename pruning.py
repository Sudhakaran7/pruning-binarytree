from binarytree import build 
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root

n=int(input())
nodes =list(map(int,input().split())) 
binary_tree = build(nodes) 
val=Solution()
print(val.pruneTree(binary_tree))