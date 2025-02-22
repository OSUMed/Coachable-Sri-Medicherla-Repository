class Solution:

    def recursion(self, items, depth, global_sum):
        for item in items:
            if item.isInteger():
                global_sum[0] += item.getInteger() * depth
            else:
                if type(item) == 'precompiled.nestedinteger.NestedInteger':
                    print(True)
                print(type(item))
                self.recursion(item.getList(), depth+1, global_sum)

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        global_sum = [0]
        depth = 1
        self.recursion(nestedList, depth, global_sum)
        return global_sum[0]
