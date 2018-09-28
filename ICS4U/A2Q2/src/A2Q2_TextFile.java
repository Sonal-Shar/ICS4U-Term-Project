import java.util.Random;

public class A2Q2_TextFile {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random rand = new Random(); 
		A2Q2_IO.createOutputFile("file02.txt");
		
		
		for(int i =0; i < 100; i++)
			A2Q2_IO.println(rand.nextInt(10 + 1));
		A2Q2_IO.closeOutputFile();
	}
}
