class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_walker, q_walker = p, q

        while p_walker != q_walker:
            p_walker = p_walker.parent if p_walker.parent else q
            q_walker = q_walker.parent if q_walker.parent else p
        
        return p_walker
        
        