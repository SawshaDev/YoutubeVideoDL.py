from pytube import YouTube
import os


def downloadMP4(URL):
    video = YouTube(URL)
    video_streams1 = video.streams.filter(file_extension='mp4').get_by_itag(22)
    #video_streams2 = video.streams.filter(only_audio=True).get_by_itag(139)
    name = video_streams1.title
    ftype = "mp4"

    if os.path.exists(f"video/{name}.{ftype}"):
        return("File {name}.{ftype} Exists")
        
    else:    
        if ftype == "mp4":
            video_streams1.download(filename=f"{name}.mp4",
            output_path = "video")
          



def downloadMP3(URL):
    video = YouTube(URL)
    video_streams2 = video.streams.filter(only_audio=True).get_by_itag(139)
    name = video_streams2.title
    ftype = "mp3"

    if os.path.exists(f"video/{name}.{ftype}"):
        return("File {name}.{ftype} Exists")
        
    else:
        video_streams2.download(filename=f"{name}.mp3",
        output_path = "video")

