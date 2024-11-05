# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node, freq_map):
            if not node:
                return 

            freq_map[node.val] = freq_map.get(node.val, 0) + 1

            dfs(node.left , freq_map)
            dfs(node.right, freq_map)

            return freq_map

        freq_map = dfs(root, {})

        # print(freq_map)
        sorted_dict = dict(sorted(freq_map.items(), key = lambda x:x[1], reverse=True))
        keys = list(sorted_dict.keys())

        modes= set()
        modes.add(keys[0])
        max_value = sorted_dict[keys[0]]
        for key, value in sorted_dict.items():
            if value == max_value:
                modes.add(key)
            elif value < max_value:
                break

        return list(modes)




        


        