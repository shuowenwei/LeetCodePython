
// ; 本帖最后由 djmiss 于 2020-2-6 08:11 编辑
// ; 感觉这题其实比295，480还要简单一点。
// ; 我的想法是维护两个pq，把5%的最小数和最大数放进去。在维护一个TreeSet放中间的数
// ; 如果数据量太大，就存Pair<value, count>, 再不行就用分布式分段计算
import java.util.*;
public class Test {
PriorityQueue<Integer> bottom;
    PriorityQueue<Integer> top;
    TreeSet<Integer> middle;
    int totalSize;
    int percentage;
    int sumOfMiddle;
//     /** initialize your data structure here. */
    public Test() {
        bottom = new PriorityQueue<>((a, b)-> b.compareTo(a));
        top = new PriorityQueue<>();
        middle = new TreeSet<>();
        totalSize = 0;
        percentage = 5;
        sumOfMiddle = 0;
    }
   
    public void addNum(int num) {
        middle.add(num);
        totalSize++;
        sumOfMiddle += num;
        rebalanceBottom();
        rebalanceTop();
    }
   
    public double findAverage() {
        return (double)sumOfMiddle / middle.size();
    }
    private void rebalanceBottom() {
        int bottomSize = percentage * totalSize / 100;
        //put one more to bottomHeap
        if (bottomSize > bottom.size()) {
            int num = middle.pollFirst();
            bottom.add(num);
            sumOfMiddle -= num;
        } else {
            //same size:
            int num = middle.pollFirst(); //pull out the smallest number
            bottom.offer(num);
            sumOfMiddle -= num;
            num = bottom.poll(); //pull in the biggest value
            middle.add(num);
            sumOfMiddle += num;
        }
    }
    private void rebalanceTop() {
        int topSize = percentage * totalSize / 100;
        //put one more to topHeap
        if (topSize > top.size()) {
            int num = middle.pollLast();
            top.add(num);
            sumOfMiddle -= num;
        } else {
            //same size:
            int num = middle.pollLast(); //pull out the largest number
            top.offer(num);
            sumOfMiddle -= num;
            num = top.poll(); //pull in the smallest value
            middle.add(num);
            sumOfMiddle += num;
        }
    }
    public static void main(String args[]) {
      Test t = new Test();
      for (int i = 0; i < 200; i++) {
        t.addNum(i);
        System.out.println("i=" +i+ ", avg="+ t.findAverage());
        System.out.print("number removed in top: ");
        for (int j: t.top) {
          System.out.print(j + " ");
        }
        System.out.println();
        
        System.out.print("number removed in bottom: ");
        for (int j: t.bottom) {
          System.out.print(j + " ");
        }
        System.out.println();
      }
      for (int i = 100; i >= 0; i--) {
        t.addNum(i);
        System.out.println("i=" +i+ ", avg="+ t.findAverage());
        System.out.print("number removed in top: ");
        for (int j: t.top) {
          System.out.print(j + " ");
        }
        System.out.println();
        
        System.out.print("number removed in bottom: ");
        for (int j: t.bottom) {
          System.out.print(j + " ");
        }
        System.out.println();
      }
   }
}