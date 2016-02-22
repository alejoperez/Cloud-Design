from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from hello.models import Design

def resizeImage(design):
    image = Image.open(design.imageFile)
    image = image.resize((800, 600), Image.ANTIALIAS)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype("arial.ttf", 15)
    draw.text((0, 0),str(design.designer.name)+' '+str(design.created_date),(255,255,255))
    image.save(str(design.imageFile).replace('.jpg','_M.png').replace('.jpeg','_M.png').replace('.JPG','_M.png').replace('.JPEG','_M.png'), quality=90)
