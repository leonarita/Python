from pytube import YouTube

YouTube("https://www.youtube.com/watch?v=KKtb0K0Ejcw&feature=emb_logo").streams.first().download()