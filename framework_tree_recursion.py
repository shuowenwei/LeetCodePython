# https://labuladong.gitee.io/algo/1/2/

# /* 基本的二叉树节点 */
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse(root: TreeNode):
    traverse(root.left)
    traverse(root.right)


# /* 基本的 N 叉树节点 */
class N_TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = []
def traverse(root: N_TreeNode):
    for child in root.N_TreeNode: 
        traverse(root.right)



def traverse(root: TreeNode):
    # 前序遍历代码位置
    traverse(root.left)
    # 中序遍历代码位置
    traverse(root.right)
    # 后序遍历代码位置


