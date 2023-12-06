""" Python app developed by Abraham Chavez to download Youtube videos as mp3 or mp4 files, future uptades will include a GUI progress bar and compatibility for more formats"""
from pytube import YouTube
import os

def downloadYoutubeMP4(vid_url, path):
    yt = YouTube(vid_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    if not os.path.exists(path):
        os.makedirs(path)

    yt.download(path)

def downloadYoutubeMP3(vid_url, path):
    yt = YouTube(vid_url)
    yt = yt.streams.filter(only_audio=True).first()
    
    if not os.path.exists(path):
        os.makedirs(path)

    #Add mp3 extension to file
    path = path + '\\' + yt.title + '.mp3'
    yt.download(path)

url = input('Input url: ')

# Use raw string (r"") to avoid issues with backslashes
path = r"C:\Users\abrah\Desktop\Downloader"
format = input('Input format (mp3/mp4): ')

if format == 'mp3':
    downloadYoutubeMP3(url, path)
elif format == 'mp4':
    downloadYoutubeMP4(url, path)
