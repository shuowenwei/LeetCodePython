
import java.lang.reflect.Field;

public class ReflectionTutorial {

    public static void main(String[] args){
        Cat myCat = new Cat("Stella", 6); 

        Field[] catFields = myCat.getClass().getDeclaredFields();

        for (Field field : catFields) {
            // System.out.println(field.getName());
            if (field.getName().equals("name")){
                field.set(myCat, "Jimmy McGill");
            }
        }
    }
}
