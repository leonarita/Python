from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open("codeGoogle.svg"))

print(d[0].data.decode())