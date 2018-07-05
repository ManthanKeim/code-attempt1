from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=rrERfSqzt2k")
yt = yt.get('mp4', '720p')
yt.download('C:\Users\Bhavik Chopra\Desktop')