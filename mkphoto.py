import PIL
import datetime
import os
from PIL import Image, ImageDraw, ImageFont
from time import strftime, gmtime
from time import sleep



d1 = -1
d2 = 0
d3 = 0
d4 = 0
d5 = ""
while d1 <= 59:
	d1 += 1
	d6 = f"{d4}{d2}:{d5}{d3}{d1}"
	d7 = d6.replace(':', "_")
	sleep(0)
	print(f"{d6}.png Успешно создано")
	
	img = Image.open(r'resource/background.jpg') 
	
	draw = ImageDraw.Draw(img) 
	text = f"{d6}"
	
	font = ImageFont.truetype(r'resource/timefont.otf', 300)
	
	textwidth, textheight = draw.textsize(text, font)
	width, height = img.size 
	x=width/2-textwidth/2
	y=height/2.3-textheight/2.3
	
	draw.text((x, y), text, font=font) 
	
	img.save(r'src' + d7 + ".png")

	
	
	
	
	if d1 == 9:
		d3 = ""
	
	if d1 == 0:
		d3 = 0
		d5 = ""
		
	if d2 == 0:
		d4 = 0
		d5 = ""

	if d1 == 59:
		d2 += 1
		d1 = -1
		d5 = 0
		if d2 == 10:
			d4 = ""
		

	if d2 == 24:
		break
		

