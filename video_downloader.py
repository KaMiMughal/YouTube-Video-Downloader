import pyfiglet
import pytube

text = pyfiglet.figlet_format("YouTube Video Downloader")
print(text)

video_url = input("Enter The URL of the Youtube Video: ")

yt = pytube.YouTube(video_url)
for i, stream in enumerate(yt.streams):
    print(f"{i}:{stream.resolution}")

resolution = int(input("Enter the number of the video resolution you want to download: "))

video = yt.streams[resolution]

video.download("/Desktop")

print("Video downloaded successfully!\nPlease check the video in your download folder")