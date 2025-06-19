# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # Global maximum path sum

        def dfs(node):
            if not node:
                return 0

            # Recursively get max path sum from left/right, ignore negative paths
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Path passing through this node (may be the best one!)
            current_path_sum = node.val + left_gain + right_gain

            # Update global max if this path is better
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the max path sum that can be extended to parent
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum