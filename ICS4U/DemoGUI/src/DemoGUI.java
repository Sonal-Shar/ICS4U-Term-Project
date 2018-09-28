import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class DemoGUI extends JFrame implements ActionListener{
		private JButton button;
		private JTextArea area;
		
		public DemoGUI() {
			this.setSize(600,400);
			this.setResizable(false);
			this.setLayout(null);
			this.setTitle("GUI DEMO");
			
			Container c = getContentPane();
			c.setBackground(new Color(175,0,175));
			
			this.setVisible(true);
			this.setDefaultCloseOperation(EXIT_ON_CLOSE);
			
			
			JLabel titleLabel = new JLabel("Demo-ing GUIs");
			//x pos, y pos, width, height
			titleLabel.setBounds(0, 10, getWidth(), 40);
			titleLabel.setFont(new Font("Old English",Font.BOLD, 26));
			titleLabel.setForeground(Color.WHITE);
			titleLabel.setHorizontalAlignment(JLabel.CENTER);
			c.add(titleLabel);
			
			area = new JTextArea();
			area.setBounds(360,70,215,100);
			area.setLineWrap(true);
			area.setWrapStyleWord(true);
			area.setFont(new Font("Georgia", Font.PLAIN, 15));
			c.add(area);
			
			button = new JButton("CLICK ME");
			button.setBounds(10,100,240,100);
			button.setOpaque(false);
			button.addActionListener(this);
			
			c.add(button);
		}
		
		public void actionPerformed(ActionEvent e) {
			if(e.getSource()== button) 
				area.setText("Boop!");
			
		}
		
		public static void main(String[] args) {
			DemoGUI gui = new DemoGUI();
		}
	}


