# https://labuladong.gitee.io/algo/1/2/

# /* 基本的数组 */
def traverse(arr):
    for i in range(len(arr)):
        # // 迭代访问 arr[i]
        pass 


# /* 基本的单链表节点 */
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None 

def traverse(head: ListNode):
    p = head 
    while p is not None:
        # // 迭代访问 p.val
        p = p.next 

def traverse(head: ListNode):
    # // 递归访问 head.val
    traverse(head.next)

# 链表兼具递归结构，树结构不过是链表的衍生。那么，链表其实也可以有前序遍历和后序遍历：
def traverse(head: ListNode):
    # // 前序遍历代码
    traverse(head.next)
    # // 后序遍历代码


# 1、合并两个有序链表
# 2、合并 k 个有序链表
# 3、寻找单链表的倒数第 k 个节点
# 4、寻找单链表的中点
# 5、判断单链表是否包含环并找出环起点
# 6、判断两个单链表是否相交并找出交点

# LeetCode examples:
# 21.合并两个有序链表（简单）
# 23.合并K个升序链表（困难）
# 141.环形链表（简单）
# 142.环形链表 II（中等）
# 876.链表的中间结点（简单）
# 160.相交链表（简单）
# 19.删除链表的倒数第 N 个结点（中等）