import java.util.Scanner;

public class AssignmentOne {

	public static void main(String[] args) {
		String name;
		String age;
		String address;
		
		Scanner scan1 = new Scanner(System.in);
				
		//Ask for user's name
		System.out.print("What's your name?");
				
		name = scan1.nextLine(); //READ STRINGS ONLY
		
		//Ask for user's age
		System.out.print("How old are you?");
		age = scan1.nextLine();
				
		//Output the info
		System.out.print("Where do you live?");
		address = scan1.nextLine();
		
		System.out.print("Hi " + name + "! You are " + age + "years old and you live at " + address + "!");
				
		scan1.close();

	}

}
