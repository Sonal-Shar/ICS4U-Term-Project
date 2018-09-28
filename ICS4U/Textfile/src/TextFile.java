import java.util.Scanner;

public class TextFile {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		IO.createOutputFile("FirstFile.txt");
		IO.print("I am awesome!");
		IO.closeOutputFile();
		
 		Scanner user_input = new Scanner( System.in );
 		IO.createOutputFile("Attempt.txt");
		String name = user_input.nextLine();
		IO.println(name);
		user_input.close();
		IO.closeOutputFile();
		
		
		IO.createOutputFile("HighScores.txt");
		IO.println("Mouse: 14 seconds");
		IO.println("Forar: 8 seconds");
		IO.closeOutputFile();
		
		
		IO.createOutputFile("HighScores.txt", true);
		IO.println("Cheetah: 0.1 seconds");
		IO.closeOutputFile();
		
		
		//first we need to count how many lines there are in the file
		IO.openInputFile("HighScores.txt");
		
		String line = IO.readLine();
		
		int numLines = 0;
		
		while(line !=null)
		{
			System.out.print(line.toUpperCase());
			numLines++;
			line = IO.readLine();
		}
		
		System.out.println(numLines);
		IO.closeInputFile();
		
		//Now we can store these lines in an array
		
		String[] highScores = new String[numLines];
		
		IO.openInputFile("HighScores.txt");
		for (int i = 0; i < numLines; i ++)
			highScores[i] = IO.readLine();
		IO.closeInputFile();
		
		//Now we can do things with the data
		for (int i = 0; i < numLines; i++)
			System.out.println(highScores[i].toLowerCase());
	}

}
