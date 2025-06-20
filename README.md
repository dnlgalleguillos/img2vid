# Image to Video Converter

This Python script uses FFmpeg to convert a single image into a 5-second .mp4 video with a resolution of 1920x1080 (Full HD).

## Dependencies

- Python 3
- FFmpeg

## Installation of FFmpeg

Ensure FFmpeg is installed and accessible in your system's PATH.

### On Fedora Linux:
```bash
sudo dnf install ffmpeg
```

### On Debian/Ubuntu:
```bash
sudo apt update
sudo apt install ffmpeg
```

## Usage

```bash
python image_to_video.py <path_to_your_image> [options]
```

**Arguments:**
- `input_image`: Path to the input image file (e.g., `sample.jpg`, `images/my_photo.png`). This is a required argument.

**Options:**
- `-o OUTPUT_VIDEO`, `--output OUTPUT_VIDEO`: Path for the output video file (e.g., `my_video.mp4`). If not specified, the output will be named after the input image with an `.mp4` extension (e.g., if input is `photo.jpg`, output will be `photo.mp4`).

**Example:**

```bash
python image_to_video.py sample.jpg
```

This will create `sample.mp4` in the same directory.

```bash
python image_to_video.py assets/landscape.png -o videos/landscape_video.mp4
```
This will use `assets/landscape.png` as input and create `videos/landscape_video.mp4`.

## Video Specifications
- Duration: 5 seconds
- Resolution: 1920x1080
- Format: MP4 (H.264 codec)
- Pixel Format: yuv420p (for wide compatibility)
- Scaling: The image is scaled to fit within 1920x1080 while maintaining its aspect ratio. Black bars will be added if the aspect ratio does not match 16:9.
