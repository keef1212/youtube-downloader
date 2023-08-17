from pytube import YouTube

def download_youtube_video(url, filename):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # You can change this to get a different resolution
        video.download(filename=filename)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube URL: ")
    video_filename = "video.mp4"
    
    download_youtube_video(video_url, video_filename)
