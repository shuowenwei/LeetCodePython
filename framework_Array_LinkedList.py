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