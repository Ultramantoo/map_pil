from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw, ImageFont

im = Image.open('mode_001.jpg')
draw = ImageDraw.Draw(im)
fnt_1 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 50)
fnt_2 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 40)
fnt_3 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 85)
fnt_4 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 30)
fnt_5 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttf', 30)

draw.text((155, 28), u'13413059247', fill=(27, 27, 27), font=fnt_1)
draw.text((428, 167), u'01-18 星期五', fill=(180, 180, 180), font=fnt_2)

draw.text((277, 493), u'13413059247', fill=(59, 149, 233), font=fnt_3)

draw.text((848, 1369), u'13:25', fill=(143, 167, 138), font=fnt_4)
draw.text((172, 1581), u'13:29', fill=(146, 146, 146), font=fnt_4)

im.show()
im.save('初版图片.jpg')