import calliTube
import os


def main():
    URL = input("Input url here: ")
    video = YouTube(URL)
    video_streams1 = video.streams.filter(file_extension='mp4').get_by_itag(22)
    video_streams2 = video.streams.filter(only_audio=True).get_by_itag(139)
    print(video_streams1.title)
    name = video_streams1.title
    ftype = input("MP4 or MP3: ").lower()

    if os.path.exists(f"video/{name}.{ftype}"):
        print("File {name}.{ftype} Exists")
        main()
        
    else:
        if ftype == "mp3":
            video_streams2.download(filename = f"{name}.mp3", 
            output_path = "video") 
            
            
        if ftype == "mp4":
            video_streams1.download(filename=f"{name}.mp4",
            output_path = "video")
            