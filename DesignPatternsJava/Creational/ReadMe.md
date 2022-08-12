refer to https://www.javatpoint.com/factory-method-design-pattern
## Factory Method Pattern
A Factory Pattern or Factory Method Pattern says that just define an interface or abstract class for creating an object but let the subclasses decide which class to instantiate. In other words, subclasses are responsible to create the instance of the class.

The Factory Method Pattern is also known as Virtual Constructor.

## Advantage of Factory Design Pattern
- Factory Method Pattern allows the sub-classes to choose the type of objects to create.
- It promotes the loose-coupling by eliminating the need to bind application-specific classes into the code. That means the code interacts solely with the resultant interface or abstract class, so that it will work with any classes that implement that interface or that extends that abstract class.

## Usage of Factory Design Pattern
- When a class doesn't know what sub-classes will be required to create
- When a class wants that its sub-classes specify the objects to be created.
- When the parent classes choose the creation of objects to its sub-classes.

Categorization of design patterns:
Basically, design patterns are categorized into two parts:

Core Java (or JSE) Design Patterns.
- JEE Design Patterns.
- Core Java Design Patterns

In core java, there are mainly three types of design patterns, which are further divided into their sub-parts:

## 1.Creational Design Pattern
- Factory Pattern
- Abstract Factory Pattern
- Singleton Pattern
- Prototype Pattern
- Builder Pattern.
## 2. Structural Design Pattern
- Adapter Pattern
- Bridge Pattern
- Composite Pattern
- Decorator Pattern
- Facade Pattern
- Flyweight Pattern
- Proxy Pattern
## 3. Behavioral Design Pattern
- Chain Of Responsibility Pattern
- Command Pattern
- Interpreter Pattern
- Iterator Pattern
- Mediator Pattern
- Memento Pattern
- Observer Pattern
- State Pattern
- Strategy Pattern
- Template Pattern
- Visitor 


# JEE or J2EE Design Patterns
J2EE design patterns are built for the developing the Enterprise Web-based Applications.

In J2EE , there are mainly three types of design patterns, which are further divided into their sub-parts:

# 1. Presentation Layer Design Pattern
- Intercepting Filter Pattern
- Front Controller Pattern
- View Helper Pattern
- Composite View Pattern
# 2. Business Layer Design Pattern
- Business Delegate Pattern
- Service Locator Pattern
- Session Facade Pattern
- Transfer Object Pattern
# 3. Integration Layer Design Pattern
- Data Access Object Pattern
- Web Service Broker Pattern