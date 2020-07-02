import pytube

# url = str(input("\n\n\tInsira a URL do vídeo que deseja baixar no YouTube: "))
url = "https://www.youtube.com/watch?v=HtR8UIfUeqM"

video = pytube.YouTube(url)
youtube = video.streams.first()
youtube.download(r'C:\Users\leo_n\Downloads')
