import java.util.ArrayList;
import java.util.Arrays;

public class ArrayVsArrayList {
    public static void main(String[] args) {

        String[] friendsArray = new String[4]; // size is fixed
        String[] friendsArray2 = {"John", "Chris", "Eric", "Luke"}; // size is not fixed

        ArrayList<String> friendsArrayList = new ArrayList<>(); // no fixed size
        ArrayList<String> friendsArrayList2 =
                new ArrayList<>(Arrays.asList("John", "Chris", "Eric", "Luke"));

        System.out.println(friendsArray2[1]);
        System.out.println(friendsArrayList2.get(1));

        System.out.println(friendsArray2.length);
        System.out.println(friendsArrayList2.size());

    }
}
