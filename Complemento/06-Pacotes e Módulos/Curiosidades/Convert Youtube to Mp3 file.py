import youtube_dl


class YTD2MP3:
    def __init__(self):
        self.yd1 = youtube_dl.YoutubeDL(self.getOptions())

    def hook(self, d):
        if d['status'] == 'finished':
            print('Done downloading. Converting now...')

    def getOptions(self):
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
            'progress_hooks': [self.hook],
        }

    def startDownload(self, url):
        self.yd1.download([url]);


downloader = YTD2MP3()
url = input("Enter Youtube URL:")
downloader.startDownload(url)
