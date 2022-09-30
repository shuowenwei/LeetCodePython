import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SimpleCalculatorTest  {

    @Test
    void twoPlusTwoShouldEqualFour(){
        // var calculator = new SimpleCalculator();
       SimpleCalculator calculator = new SimpleCalculator();
        assertEquals(calculator.add(2,2), 4);
    }
}