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


# 리스트 누적 없는 보다 간결한 버전

class Solution2:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            # 리프 노드에 도달한 경우
            if not node.left and not node.right:
                return current_sum

            # 왼쪽과 오른쪽 재귀 호출 결과 합산
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)
