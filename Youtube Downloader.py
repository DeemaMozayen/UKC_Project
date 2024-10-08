from pytube import YouTube
import os
import time
import subprocess
from pytube.cli import on_progress

yt = YouTube('https://www.youtube.com/watch?v=OXQwx1EolD8', on_progress_callback=on_progress)
print("")
print("Downloading", '"{}"'.format(yt.title))

yt.streams.filter(progressive = True, file_extension = "mp4").first().download()

print("")
print("Download Successful!\n")

time.sleep(1.5)
print("Opening -", '"{}"'.format(yt.title), "\n")
subprocess.run(["open", f"{yt.title}.mp4"])
#os.startfile(f"{yt.title}mp4")
#time.sleep(yt.length)