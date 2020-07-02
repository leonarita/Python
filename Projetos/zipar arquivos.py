import zipfile

jungle_zip = zipfile.ZipFile('D:\\Vestibular\\Matemática.zip', 'w')
jungle_zip.write('D:\Vestibular\Matemática', compress_type=zipfile.ZIP_DEFLATED)

jungle_zip.close()