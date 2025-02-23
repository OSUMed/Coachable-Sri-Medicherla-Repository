import collections
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer_hash = collections.defaultdict(list)
        minimum = float("inf")
        maximum = float("-inf")

        queue = collections.deque([(0, root)])

        while queue:
            value, node = queue.popleft()

            minimum = min(minimum, value)
            maximum = max(maximum, value)

            answer_hash[value].append(node.val)

            if node.left:
                queue.append((value - 1, node.left))

            if node.right:
                queue.append((value + 1, node.right))
    
        res = []
        for i in range(minimum, maximum+1):
            res.append(answer_hash[i])
        
        return res
        
