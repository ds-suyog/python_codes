import sys
from PIL import Image

#imgFile = "c1a.png"
imgFile = sys.argv[1]
im = Image.open(imgFile, 'r')
#print im.size
pix_val = list(im.getdata())
pix_val2 = pix_val[:]

for i in range(0,len(pix_val2)):
  if sum(pix_val2[i]) >=300:
    pix_val2[i] = (255,255,255)

im2 = Image.new(im.mode, im.size)
im2.putdata(pix_val2)
im2.show()

im2.save(imgFile.split(".")[0] + "_cleaned.png","PNG")

