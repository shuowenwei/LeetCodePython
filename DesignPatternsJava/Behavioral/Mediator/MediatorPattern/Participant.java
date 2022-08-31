package DesignPatternsJava.Behavioral.Mediator.MediatorPattern;

public abstract class Participant {
	
	public abstract void sendMsg(String msg);

	public abstract void setname(String name);
	
	public abstract String getName();

}
