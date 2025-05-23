from pytubefix import YouTube

url = input("Enter the YouTube video URL: ")
yt = YouTube(url)

print("Title:", yt.title)
print("Length:", yt.length, "seconds")
print("Views:", yt.views)

stream = yt.streams.get_highest_resolution()
print("Downloading...")
stream.download()
print("Download complete!")
