# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_list = []
        def dfs(str_num, node):
            if not node:
                return

            str_num += str(node.val)

            if not node.left and not node.right:
                sum_list.append(str_num)
                return

            dfs(str_num, node.left)
            dfs(str_num, node.right)
            
        dfs('', root)

        return sum(int(str_num) for str_num in sum_list)