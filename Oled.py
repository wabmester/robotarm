import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24

class Oled:
	def __init__(self):
		# 128x64 display with hardware I2C:
		self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
		self.disp.begin()

		# Clear display.
		self.disp.clear()
		self.disp.display()


	def drawOutline(self):  
		# Create blank image for drawing.
		# Make sure to create image with mode '1' for 1-bit color.
		width = self.disp.width
		height = self.disp.height
		image = Image.new('1', (width, height))

		# Get drawing object to draw on image.
		draw = ImageDraw.Draw(image)

		# Draw a black filled box to clear the image.
		draw.rectangle((0,0,width,height), outline=0, fill=0)

		# Display image.
		self.disp.image(image)
		self.disp.display()

	def drawShapes(self):
		width = self.disp.width
		height = self.disp.height
		image = Image.new('1', (width, height))
		# Get drawing object to draw on image.
		draw = ImageDraw.Draw(image)
		# Draw some shapes.
		# First define some constants to allow easy resizing of shapes.
		padding = 2
		shape_width = 20
		top = padding
		bottom = height-padding
		# Move left to right keeping track of the current x position for drawing shapes.
		x = padding
		# Draw an ellipse.
		draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
		x += shape_width+padding
		# Draw a rectangle.
		draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
		x += shape_width+padding
		# Draw a triangle.
		draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
		x += shape_width+padding
		# Draw an X.
		draw.line((x, bottom, x+shape_width, top), fill=255)
		draw.line((x, top, x+shape_width, bottom), fill=255)
		x += shape_width+padding

		# Display image.
		self.disp.image(image)
		self.disp.display()

# Main program logic follows:
if __name__ == '__main__':
	print ('Program is starting ... ')
	disp=Oled()
	disp.drawOutline()
	disp.drawShapes()
