import java.util.ArrayList;
import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args){
        LinkedList<String> namesLinkedList = new LinkedList<>();
        namesLinkedList.add("John");
        namesLinkedList.add("Paul");
        namesLinkedList.add("George");
        namesLinkedList.add("Ringo");
        System.out.println(namesLinkedList.get(2));

        String[] names = new String[4]; // array is has a fixed size
        ArrayList<String> namesArrayList = new ArrayList<>(); // default size is 10?
        namesArrayList.add("John");
        namesArrayList.add("Paul");
        namesArrayList.add("George");
        namesArrayList.add("Ringo");
        System.out.println(namesArrayList.get(2));

    }
}
