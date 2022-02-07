# https://labuladong.gitee.io/algo/1/2/

# /* 基本的数组 */
def traverse(arr):
    for i in range(len(arr)):
        # // 迭代访问 arr[i]
        pass 


# /* 基本的单链表节点 */
class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next 

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

def reverseWholeLinkedList(head, till = None):
    pre = None 
    cur = head 
    # nxt = head 
    while cur is not till:
        nxt = cur.next
        cur.next = pre
        pre = cur 
        cur = nxt 
    return pre, cur
    # pre is the new head 
    # cur is till
    
"""
class ListNode(object):
    def __init__(self, val = 0, nxt = None):
        self.val = val 
        self.next = nxt 

node6 = ListNode(6)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(0, node1)

newHead, cur = reverseWholeLinkedList(node3, node6)
while head:
    print(' -> ', head.val, end = ' ')
    head = head.next 
print()


while newHead:
    print(' -> ', newHead.val, end = ' ')
    newHead = newHead.next 
print()
print(cur.val)
print(node3)
print(node3.next)
"""
