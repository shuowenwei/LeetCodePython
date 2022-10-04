import java.util.ArrayList;
import java.util.Arrays;

public class ArrayVsArrayList {
    public static void main(String[] args) {

        String[] friendsArray = new String[4]; // size is fixed
        String[] friendsArray2 = {"John", "Chris", "Eric", "Luke"}; // size is not fixed

        ArrayList<String> friendsArrayList = new ArrayList<>(); // no fixed size
        ArrayList<String> friendsArrayList2 =
                new ArrayList<>(Arrays.asList("John", "Chris", "Eric", "Luke"));

        // Get element
        System.out.println(friendsArray2[1]);
        System.out.println(friendsArrayList2.get(1));

        // Get size
        System.out.println(friendsArray2.length);
        System.out.println(friendsArrayList2.size());

        // Add an element
        // you can't do that with Arrays
        friendsArrayList2.add("Mitch");
        System.out.println(friendsArrayList2.get(4));

        // Set an element
        friendsArray2[0] = "Carl";
        System.out.println(friendsArray2[0]);
        friendsArrayList2.set(0, "Carl");
        System.out.println(friendsArrayList2.get(0));

        // Remove an element
        // you can't do that with Arrays
        friendsArrayList2.remove(1);
        friendsArrayList2.remove("Chris");
        System.out.println(friendsArrayList2.get(1));

        // Print
        System.out.println(friendsArray); // give the physical address
        System.out.println(friendsArrayList2);
    }
}
