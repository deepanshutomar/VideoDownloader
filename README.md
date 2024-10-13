# Video Downloader for YouTube, Instagram, and Twitter

This project provides a simple command-line tool for downloading videos from YouTube, Instagram, and Twitter (now X). The program automatically detects the platform from the given link and downloads the video in the highest available resolution using the `yt-dlp` library.

## Features

- **YouTube Video Download:** Fetches the highest resolution video from YouTube.
- **Instagram Video Download:** Supports downloading videos from Instagram.
- **Twitter (X) Video Download:** Downloads videos from Twitter (X).
- **Automatic Platform Detection:** Based on the provided link, the script automatically detects the platform and downloads the video.
- **Easy to Use:** Works seamlessly in a Google Colab environment for hassle-free video downloads.

## Installation

To get started, you can use the following instructions to set up the environment and run the tool.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/video-downloader-tool.git
cd video-downloader-tool
```

### 2. Install Dependencies

You need to install `yt-dlp`, a powerful library that handles video downloading. Run the following command to install it:

```bash
pip install yt-dlp
```

## Usage

The script can be executed either in a local Python environment or in Google Colab. Follow the steps below to use it.

1. **Run the script** by executing the Python code.
2. **Input the video URL** from YouTube, Instagram, or Twitter (X) when prompted.
3. The tool will detect the platform and download the video in the highest available quality.

### Example:

```bash
Enter the video link: https://www.youtube.com/watch?v=example
Downloading highest resolution video from YouTube...
Download complete.
```

### Code Sample:

```python
# Input the video URL
video_url = input("Enter the video link: ")
detect_and_download(video_url)
```

### Google Colab Setup:

To use the tool in Google Colab:

1. Install the `yt-dlp` library:

```bash
!pip install yt-dlp
```

2. Run the provided Python script in Colab to download the video.

## Project Structure

```
video-downloader-tool/
├── README.md             # Project documentation
├── download_video.py     # Python script for downloading videos
└── requirements.txt      # Python dependencies
```

## Requirements

- Python 3.7 or higher
- `yt-dlp` library for downloading videos

### Install Dependencies:

```bash
pip install yt-dlp
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- **yt-dlp** for providing a powerful and flexible video downloading solution.
```

### Explanation:

- **Overview**: Provides a general description of the project.
- **Installation**: Steps to install `yt-dlp` and set up the environment.
- **Usage**: Describes how to run the script and download videos.
- **Google Colab Setup**: Provides guidance on running the tool in Colab.
- **Acknowledgements**: Credits the libraries used in the project.

Let me know if you need to add or modify anything further!
