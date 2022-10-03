import javax.swing.text.html.Option;
import java.util.Optional;

public class OptionalTutorial {

    public static void main(String[] args){

//        Cat myCat = findCatByName("Fred");
        Optional<Cat> optionCat = findCatByName("Fred");
//        optionCat.get().getAge();

//        if (myCat != null) {
//            System.out.println(myCat.getAge());
//        }
//        else{
//            System.out.println(0);
//        }

//        if (optionCat.isPresent()) {
//            System.out.println(optionCat.get().getAge());
//        }
//        else{
//            System.out.println(0);
//        }
        Cat myCat = optionCat.orElse(new Cat("UNKNOWN", 0));
//        Cat myCat = optionCat.orElseGet(): // lambda function
//        Cat myCat = optionCat.orElseThrow(): // lambda function
        System.out.println(optionCat.map(Cat::getAge)
                .orElse(0));
    }

    private static Optional<Cat> findCatByName(Optional<String> name){
        Cat cat = new Cat(name, 3);
        return Optional.ofNullable(cat);
    }
}
