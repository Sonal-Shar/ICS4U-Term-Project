import java.util.Scanner;


public class QuestionSix {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner user_input = new Scanner( System.in );
		
		//Ask for user input
		System.out.print("Enter your first course mark: ");
		float one = user_input.nextFloat();
		System.out.print("Enter your second course mark: ");
		float two = user_input.nextFloat();
		System.out.print("Enter your third course mark: ");
		float three = user_input.nextFloat();
		System.out.print("Enter your fourth course mark: ");
		float four = user_input.nextFloat();
		
		System.out.print(Math.floor(((one + two + three + four)/4)* 10) / 10);
	}
	
}
