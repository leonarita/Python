import pyqrcode

s = "www.google.com"

url = pyqrcode.create(s)
url.svg("codeGoogle.svg", scale=10)
