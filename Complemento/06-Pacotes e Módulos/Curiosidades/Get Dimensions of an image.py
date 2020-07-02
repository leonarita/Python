from PIL import Image

image = Image.open("img.png")
width, height = image.size

print(width, height)