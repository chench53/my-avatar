from PIL import Image, ImageDraw, ImageFont

class MyIcon():
	def __init__(self, font, letters):
		self.__font = font
		self.__1st, self.__2nd = letters # letters showld be a list of length 2, like ['a', 'b'] 

	def Draw(self, bgColor, firstColor, secondColor, size=512):
		img = Image.new('RGBA', (size, size)) # blank image
		d = ImageDraw.Draw(img)
		d.rectangle([0, 0, size-1,size-1], fill = bgColor)
		d.text([size*3/8-1,-size/16+1], self.__1st, font = self.__font, fill = firstColor)
		d.text([size*3/16-1, size/16-1], self.__2nd, font = self.__font, fill = secondColor)

		return img


# font and font-size
font = ImageFont.truetype("SourceSansPro-Bold.otf", 384)

white = '#ffffff'
blue = "#4885ed"
red = '#db3236'
yellow = '#f4c20d'
green = '#3cba54'
revolution_red = '#dd0b01'
revolution_yellow = '#faf333'
transparent = (0, 0, 0, 0)

CC_icon = MyIcon(font, ['C', 'C']) # my CC icon

			
def DrawPlain():
	img = CC_icon.Draw(blue, white, white)
	img.save('CCPlain.png', 'PNG') 

def DrawColor():
	img = CC_icon.Draw(blue, red, yellow)	
	img.save('CCColor.png', 'PNG') 

def DrawCutout():
	img = CC_icon.Draw(blue, transparent, transparent)	
	img.save('CCCutout.png', 'PNG') 	

def DrawCleanPlain():
	img = CC_icon.Draw(transparent, white, white)
	img.save('CCCleanPlain.png', 'PNG') 

def DrawCleanColor():
	img = CC_icon.Draw(transparent, red, yellow)
	img.save('CCCleanColor.png', 'PNG')

def DrawRevolution():
	img = CC_icon.Draw(revolution_red, revolution_yellow, revolution_yellow)
	img.save('CCRevolution.png', 'PNG')

def Draw2():
	img = CC_icon.Draw(
		'#333333', 
		'#db3236', 
		'#f4c20d'
		)
	img.save('CC4.png', 'PNG')

if __name__ == '__main__':
	# DrawPlain()
	# DrawColor()
	# DrawCutout()
	# DrawCleanPlain()
	# DrawCleanColor()
	# DrawRevolution()
	Draw2()
