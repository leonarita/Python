import zipfile

zf = zipfile.ZipFile("code.zip", "w")

zf.write("code.txt", compress_type=zipfile.ZIP_DEFLATED)

zf.close()


