from PIL import Image, ImageDraw

txt = input("Enter your string: ")

img = Image.new("RGB", (200, 30), color=(73, 109, 137))

d = ImageDraw.Draw(img)
d.text((10, 10), txt, fill=(255, 255, 255))

img.save("textotoimage.png")

