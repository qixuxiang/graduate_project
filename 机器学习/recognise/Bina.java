import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
public class Bina {


    
 //    public void grayImage() throws IOException{
	// File file = new File(System.getProperty("user.dir")+"/test1.png");
	// BufferedImage image = ImageIO.read(file);
	
	// int width = image.getWidth();
	// int height = image.getHeight();
	
	// BufferedImage grayImage = new BufferedImage(width, height, BufferedImage.TYPE_BYTE_GRAY);//重点，技巧在这个参数BufferedImage.TYPE_BYTE_GRAY
	// for(int i= 0 ; i < width ; i++){
	//     for(int j = 0 ; j < height; j++){
	// 	int rgb = image.getRGB(i, j);
	// 	grayImage.setRGB(i, j, rgb);
	//     }
	// }
	
	// File newFile = new File(System.getProperty("user.dir")+"/test1.png");
	// ImageIO.write(grayImage, "png", newFile);
 //    }
    public void binaryImage() throws IOException{
	File file = new File(System.getProperty("user.dir")+"/test4hhh.png");
	BufferedImage image = ImageIO.read(file);
	
	int width = image.getWidth();
	int height = image.getHeight();
	
	BufferedImage grayImage = new BufferedImage(width, height, BufferedImage.TYPE_BYTE_BINARY);//重点，技巧在这个参数BufferedImage.TYPE_BYTE_BINARY
	for(int i= 0 ; i < width ; i++){
	    for(int j = 0 ; j < height; j++){
		int rgb = image.getRGB(i, j);
		grayImage.setRGB(i, j, rgb);
	    }
	}
	
	File newFile = new File(System.getProperty("user.dir")+"/test4hj.png");
	ImageIO.write(grayImage, "png", newFile);
    }
    
    public static void main(String[] args) throws IOException {
	Bina demo = new Bina();
	
	demo.binaryImage();
    }

}
