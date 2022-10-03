public class OptionalTutorial {

    public static void main(String[] args){

        Cat myCat = findCatByName("Fred");

        if (myCat != null)
        System.out.println(myCat.getAge());
    }

    private static Cat findCatByName(String name){
        Cat cat = new Cat(name, 3);
        return cat;
    }
}


