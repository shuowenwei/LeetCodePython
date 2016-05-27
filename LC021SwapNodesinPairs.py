# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/swap-nodes-in-pairs/

"""
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
            ListNode cur = head, next1, next2;
            if(head == null) return null;
            if(head.next == null) return head;

            //head change with next is a special case, so we deal with it first
            ListNode temp = cur.next;
            cur.next = temp.next;
            temp.next = cur;
            head = temp;

            while(cur.next != null && cur.next.next != null) {
                next1 = cur.next;
                next2 = cur.next.next;
                swap(cur,next1,next2);
                cur = cur.next.next;
            }
            return head;
        }

        private void swap(ListNode cur, ListNode next1, ListNode next2) {
            cur.next = next2;
            next1.next = next2.next;
            next2.next = next1;
        }
        
}
