from StringIO import StringIO
import urllib2

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from hello.models import Design

def resizeImage(design):
    image_buff = urllib2.urlopen(str(design.imageFile)).read()
    image = Image.open(StringIO(image_buff))
    image = image.resize((800, 600), Image.ANTIALIAS)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype("arial.ttf", 15)
    draw.text((350, 570),str(design.designer.name)+' '+str(design.created_date),(255,255,255))
    image.save(str(design.imageFile).replace('.jpg','_M.png').replace('.jpeg','_M.png').replace('.JPG','_M.png').replace('.JPEG','_M.png').replace('.png','_M.png'), quality=90)
