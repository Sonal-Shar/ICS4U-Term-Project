import java.util.Scanner;

public class Intro {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello World");
		System.out.println("New line?");
		//Scanner user_input = new Scanner( System.in );
		
		String name;
		String movie;
	
		Scanner scan1 = new Scanner(System.in);
		
		//Ask for user input
		System.out.print("Enter your name: ");
		
		//Read input from keyboard and store it in a variable
		
		name = scan1.nextLine(); //READ STRINGS ONLY
		
		System.out.print("Enter your favourite movie: ");
		movie = scan1.nextLine();
		
		//Output the info
		
		System.out.print("Hi " + name + "! I like " + movie + " too!");
		
		scan1.close();
	}

}
