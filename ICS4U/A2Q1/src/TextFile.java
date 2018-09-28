import java.util.Scanner;

public class TextFile {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		IO.createOutputFile("file01.txt");
		IO.println("I am awesome!");
		Scanner user_input = new Scanner( System.in );
		String name = user_input.nextLine();
		IO.println(name);
		user_input.close();
		IO.closeOutputFile();
		
		IO.openInputFile("file01.txt");
		
		String line = IO.readLine();
		System.out.print(line);
		
	}
}