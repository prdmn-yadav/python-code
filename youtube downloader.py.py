from pytube import YouTube
link = str(input("Enter the URL :"))
ut = YouTube(link)
# Title of video
print("Title :", ut.title)
# printing all the available streams
print(ut.streams)
print(ut.streams.filter(only_video=True))
u_stream = ut.streams.get_highest_resolution()
# Starting download
print("Downloading...")
u_stream.download()
print("Download completed!!")