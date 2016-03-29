import StringIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from hello.models import Design
import urllib, cStringIO

Image.LOAD_TRUNCATED_IMAGES = True

def resizeImage(design):
    #buff = StringIO.StringIO()
    #buff.write(open(str('https://s3-us-west-2.amazonaws.com/cloud-images-andes/'+design.imageFile), 'rb').read())
    #image = Image.open(buff)
    file = cStringIO.StringIO(urllib.urlopen('https://s3-us-west-2.amazonaws.com/cloud-images-andes/'+str(design.imageFile)).read())
    image = Image.open(file)

    #image = image.resize((800, 600), Image.ANTIALIAS)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype("arial.ttf", 15)
    draw.text((350, 570),str(design.designer.name)+' '+str(design.created_date),(255,255,255))
    image.save(str(design.imageFile).replace('.jpg','_M.png').replace('.jpeg','_M.png').replace('.JPG','_M.png').replace('.JPEG','_M.png').replace('.png','_M.png'), quality=90)
