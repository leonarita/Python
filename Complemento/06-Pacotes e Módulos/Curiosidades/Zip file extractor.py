from zipfile import ZipFile

filezip = "code.zip"

with ZipFile(filezip, "r") as zip:

    zip.printdir()
    zip.extractall()


