import java.util.Scanner;

public class QuestionFour {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner user_input = new Scanner( System.in );
		
		//Ask for user input
		System.out.print("What's your name? ");
		String name = user_input.nextLine();
		System.out.print("What's your age? ");
		int age = user_input.nextInt();
		System.out.print("What year is it? ");
		int year = user_input.nextInt();
		
		int ageTwentyFive = (25- age) + year;
		int ageFifty = (50- age) + year;
		int ageSeventyFive = (75 - age) + year;
		
		System.out.print("Hello " + name + "! In " + ageTwentyFive + ", you'll be 25, in "+ ageFifty + ", you'll be 50 and in " + ageSeventyFive + ", you'll be 75");
	}
}
