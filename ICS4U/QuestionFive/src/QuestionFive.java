import java.util.Scanner;

public class QuestionFive {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner user_input = new Scanner( System.in );
				
		//Ask for user input
		System.out.print("Input your first integer. ");
		int first = user_input.nextInt();
		System.out.print("Input your second integer. ");
		int second = user_input.nextInt();
		System.out.println("Here are the basic calculations for your integers using the basic math operations:");
		System.out.println(first + "+" + second + "=" + (first + second));
		System.out.println(first + "-" + second + "=" + (first - second));
		System.out.println(first + "*" + second + "=" + (first * second));
		System.out.println(first + "/" + second + "=" + (first / second));
		System.out.print(first + "^" + second + "=" +  (int) Math.pow(first,second));
	}

}
