""" Python app developed by Abraham Chavez to download Youtube videos as mp3 or mp4 files, future uptades will include a GUI progress bar and compatibility for more formats"""
from pytube import YouTube
import os, sys, subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

        
def downloadYoutubeMP4(vid_url, path):
    yt = YouTube(vid_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    subfolder = "videos"
    full_path = os.path.join(path, subfolder)

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    yt.download(full_path)

def downloadYoutubeMP3(vid_url, path):
    yt = YouTube(vid_url)
    yt = yt.streams.filter(only_audio=True).first()
    
    subfolder = "music"
    full_path = os.path.join(path, subfolder)

    if not os.path.exists(full_path):
        os.makedirs(full_path)


    # Download the audio stream directly in mp3 format
    yt.download(full_path, filename=f"{yt.title}.mp3")


        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        url = request.form['url']
        path = r"C:\Users\abrah\Desktop\Downloader"
        format = request.form['format']
        if format == 'mp3':
            downloadYoutubeMP3(url, path)
        elif format == 'mp4':
            downloadYoutubeMP4(url, path)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

