import os
import subprocess

# Function to download the highest available resolution video from YouTube using yt-dlp
def download_youtube_video(link):
    command = f"yt-dlp -f best {link}"
    
    print("Downloading highest resolution video from YouTube...")
    subprocess.run(command, shell=True)
    print("Download complete.")

# Function to download video from Instagram using yt-dlp
def download_instagram_video(link):
    command = f"yt-dlp -f best {link}"
    
    print("Downloading video from Instagram...")
    subprocess.run(command, shell=True)
    print("Download complete.")

# Function to download video from Twitter (X) using yt-dlp
def download_twitter_video(link):
    command = f"yt-dlp -f best {link}"
    
    print("Downloading video from Twitter...")
    subprocess.run(command, shell=True)
    print("Download complete.")

# Function to detect link and call respective downloader
def detect_and_download(link):
    if "youtube.com" in link or "youtu.be" in link:
        download_youtube_video(link)
    elif "instagram.com" in link:
        download_instagram_video(link)
    elif "twitter.com" or "x.com" in link:
        download_twitter_video(link)
    else:
        print("Unsupported URL. Please enter a valid YouTube, Instagram, or Twitter (X) link.")

# Main execution block for Google Colab
if __name__ == "__main__":
    # Input the video URL from the user
    video_url = input("Enter the video link: ")
    detect_and_download(video_url)
