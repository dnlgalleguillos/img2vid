# Image to Video Converter

## Description

This script, `image_to_video.py`, converts a single static image file into a 5-second video file. It uses FFmpeg to perform the conversion, applying scaling and padding to fit a Full HD (1920x1080) resolution while maintaining the original image's aspect ratio. A silent audio track is also included in the output video.

## Requirements

- Python 3
- FFmpeg

## Installation

1.  **FFmpeg**:
    This script requires FFmpeg to be installed on your system.
    *   On **Ubuntu/Debian-based** systems, you can install it using:
        ```bash
        sudo apt update
        sudo apt install ffmpeg
        ```
    *   On **Fedora**, you can install it using:
        ```bash
        sudo dnf install ffmpeg
        ```
    *   For other operating systems, please refer to the official FFmpeg website for installation instructions.

2.  **Python 3**:
    Python 3 is usually pre-installed on modern Linux distributions. If not, please install it using your system's package manager.

## Usage

To run the script, use the following command in your terminal:

```bash
python image_to_video.py <input_image_path> <output_video_path.mp4>
```

**Example:**

```bash
python image_to_video.py atacama_sunset.jpg atacama_sunset_video.mp4
```

Replace `atacama_sunset.jpg` with the path to your input image and `atacama_sunset_video.mp4` with the desired path for the output video.

## Output Video Specifications

-   **Format**: MP4
-   **Resolution**: 1920x1080 (Full HD)
-   **Duration**: 5 seconds
-   **Video Codec**: H.264 (libx264)
-   **Audio**: Silent AAC track

## Note on Image Aspect Ratio

The script is designed to output a video with a 16:9 aspect ratio (1920x1080).
-   If the input image's aspect ratio is already 16:9, it will be scaled to fit 1920x1080.
-   If the input image's aspect ratio is different from 16:9 (e.g., 4:3, 1:1), it will be scaled down to fit within the 1920x1080 frame while preserving its original aspect ratio. The remaining space will be filled with black bars (padding) either on the sides or top/bottom to make up the 1920x1080 resolution. This process is often referred to as "letterboxing" or "pillarboxing".
