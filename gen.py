from collections import namedtuple

from PIL import Image, ImageDraw, ImageFont

# font and font-size
font = ImageFont.truetype("SourceSansPro-Bold.otf", 384)

transparent = (0, 0, 0, 0)
white = '#ffffff'
blue = "#4885ed"
red = '#db3236'
yellow = '#f4c20d'
green = '#3cba54'
revolution_red = '#dd0b01'
revolution_yellow = '#faf333'

ColorSet = namedtuple('ColorSet', ['name', 'bgColor', 'firstColor', 'secondColor'])

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

	@property
	def name(self):
		return self.__1st + self.__2nd

CC_icon = MyIcon(font, ('C', 'C')) # my CC icon


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

def Draw4():
	img = CC_icon.Draw(
		'#E95420',
		'#AEA79F',
		'#77216F',
		)
	img.save('CCUbuntu.png', 'PNG')
e
def DrawColorSet(colorSet):
	img = CC_icon.Draw(
		colorSet.bgColor,
		colorSet.firstColor,
		colorSet.secondColor
	)
	img.save('{}_{}.png'.format(CC_icon.name, colorSet.name), 'PNG')

if __name__ == '__main__':
	pingcode = ColorSet('pingcode', (93, 207, 255), "#fff", "#348fe4")
	DrawColorSet(pingcode)
