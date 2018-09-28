import java.util.Scanner;

public class QuestionThree {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner user_input = new Scanner( System.in );
		
		//Ask for user input
		System.out.print("What's 1 + 1? ");
		float one = user_input.nextFloat();
		if(one!= 2) 
			System.out.print("Incorrect, the correct answer is 2. ");
		else {
			System.out.print("Correct, next question!");
		}
		System.out.print("What's 9 + 9? ");
		float two = user_input.nextFloat();
		if(two!= 18) 
			System.out.print("Incorrect, the correct answer is 18. ");
		else {
			System.out.print("Correct, next question!");
		}
		System.out.print("What's 75 - 25? ");
		float three = user_input.nextFloat();
		if(three!= 50) 
			System.out.print("Incorrect, the correct answer is 50. ");
		else {
			System.out.print("Correct, next question!");
		}
		System.out.print("What's 7 * 3? ");
		float four = user_input.nextFloat();
		if(four!= 21) 
			System.out.print("Incorrect, the correct answer is 21. ");
		else {
			System.out.print("Correct, next question!");
		}
		System.out.print("What's 144/12? ");
		float five = user_input.nextFloat();
		if(five!= 12) 
			System.out.print("Incorrect, the correct answer is 12. Either way, you're done. ");
		else {
			System.out.print("Correct, you're done!");
		}
	}

}