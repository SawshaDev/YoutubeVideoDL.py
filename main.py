from pytube import YouTube

URL = input("Input url here: ")  
video = YouTube(URL)
video_streams = video.streams.filter(file_extension='mp4').get_by_itag(22)
print(video_streams.title)
name = video_streams.title

video_streams.download(filename = f"{name}.mp4", 
	output_path = "video") 