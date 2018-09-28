import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;


public class IO {
	
	//VARIABLES AND METHODS NEEDED FOR WRITING TO A FILE
	
	private static PrintWriter fileOut;
	
	
	//Creates a new file (filename) in the current folder and place a reference to it in the object fileOUT
	//The parameter fileName represents the name of the Text file
	public static void createOutputFile(String filename)
	{
		createOutputFile(filename,false);
		try {  //tries to make a new text file
			fileOut = new PrintWriter(new BufferedWriter(new FileWriter(filename)));
		}
		catch(IOException e) {
			System.out.println("***Cannot create file: " + filename + " ***");
		}
	}
	
	/*Create a new file (fileName) in the current folder and places a reference to it in fileOut
	*Append TRUE if you want to add to the existing information
	*Append FALSE if you want to rewrite the entire file
	*/
	public static void createOutputFile(String fileName, boolean append) {
		try {
			fileOut = new PrintWriter(new BufferedWriter(new FileWriter(fileName, append)));
		}
		catch(IOException e) {
			System.out.println("***Cannot create file: " + fileName + " ***");
		}
	}
	
	/* Text is added to the current file
	 * String Text- the characters that will be added to the file
	 */
	public static void print(String text)
	{
		fileOut.print(text);
	}
	
	/*
	 * Text is added to the current file and then a new line is inserted at the end of the characters
	 */
	
	public static void println(String text)
	{
		fileOut.println(text);
	}
	
	// closes the file that is currently being written to
	//NOTE: MUST BE CALLED WHEN YOU ARE FINISHED TO SAVE FILE
	public static void closeOutputFile()
	{
		fileOut.close();
	}
	
	//VARIABLES AND METHODS NEEDED FOR READING FROM A FILE
	
	private static BufferedReader fileIn;
	
	/*OPENS A FILE CALLED fileNAME (file must be in the current folder)
	*Places a reference to it in fileIn
	*/
	public static void openInputFile(String fileName)
	{
		try {
			fileIn = new BufferedReader(new FileReader(fileName));
		}
		catch(FileNotFoundException e) {
			System.out.println("***Cannot open " + fileName + " ***");
		}
	}
	
	//Reads the next line from the file and returns it to be stored in a string
	public static String readLine()
	{
		try {
			return fileIn.readLine();
		}
		catch(IOException e) {
			return null;
		}
	}
	
	
	//Closes the file that is currently being read from
	public static void closeInputFile()
	{
		try {
			fileIn.close();
		}
		catch(IOException e) {}
	}
}