class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node is None:
        return []
    
    result = []
    l = [node]
    function(l, result)
    # z = []
    # for n in result:
    #     z.append(n.value)
    return result
    
    
def function(l, result):
    d = []
    if l != []:
        for n in l:
            if n.left is not None:
                d.append(n.left)
            if n.right is not None:
                d.append(n.right)
            result.append(n.value)
        # print(d)
        # result = result + l
        function(d, result)
