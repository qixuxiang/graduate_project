private static int colorToRGB(int alpha, int red, int green, int blue) {

		int newPixel = 0;
		newPixel += alpha;
		newPixel = newPixel << 8;
		newPixel += red;
		newPixel = newPixel << 8;
		newPixel += green;
		newPixel = newPixel << 8;
		newPixel += blue;

		return newPixel;

}
public static void main(String[] args) throws IOException {
	BufferedImage bufferedImage 
		= ImageIO.read(new File(System.getProperty("user.dir" + "/test4.png"));
	BufferedImage grayImage = 
		new BufferedImage(bufferedImage.getWidth(), 
						  bufferedImage.getHeight(), 
						  bufferedImage.getType());
		
	
	for (int i = 0; i < bufferedImage.getWidth(); i++) {
		for (int j = 0; j < bufferedImage.getHeight(); j++) {
			final int color = bufferedImage.getRGB(i, j);
			final int r = (color >> 16) & 0xff;
			final int g = (color >> 8) & 0xff;
			final int b = color & 0xff;
			int gray = (int) (0.3 * r + 0.59 * g + 0.11 * b);;
			System.out.println(i + " : " + j + " " + gray);
			int newPixel = colorToRGB(255, gray, gray, gray);
			grayImage.setRGB(i, j, newPixel);
		}
	}
	File newFile = new File(System.getProperty("user.dir") + "/test4j.png");
	ImageIO.write(grayImage, "jpg", newFile);
}