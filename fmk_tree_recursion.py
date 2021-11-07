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



# 思考一个二叉树节点需要做什么，到底用什么遍历顺序就清楚了。
def traverse(root: TreeNode):
    # 前序遍历代码位置
    traverse(root.left)
    # 中序遍历代码位置
    traverse(root.right)
    # 后序遍历代码位置

# 举个例子，比如说我们的经典算法「快速排序」和「归并排序」，对于这两个算法，你有什么理解？
# 如果你告诉我，快速排序就是个二叉树的前序遍历，
# 归并排序就是个二叉树的后序遍历，那么我就知道你是个算法高手了。



def BST(root: TreeNode, target: int):
    if (root.val == target): 
        # 找到目标，做点什么
        pass 
    if (root.val < target): 
        BST(root.right, target)
    if (root.val > target):
        BST(root.left, target)

