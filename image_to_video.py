#!/usr/bin/env python3

import subprocess
import os
import argparse

def create_video_from_image(image_path, output_path):
    """
    Creates a video from a single image using FFmpeg.
    """
    ffmpeg_command = [
        "ffmpeg",
        "-loop", "1",
        "-i", image_path,
        "-c:v", "libx264",
        "-t", "5",  # Duration of the video in seconds
        "-pix_fmt", "yuv420p",
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
        output_path
    ]

    try:
        print(f"Generating video from '{image_path}' to '{output_path}'...")
        process = subprocess.run(ffmpeg_command, capture_output=True, text=True, check=True)
        print("Video generated successfully!")
        if process.stdout:
            print("FFmpeg stdout:")
            print(process.stdout)
        if process.stderr: # FFmpeg often outputs info to stderr
            print("FFmpeg stderr:")
            print(process.stderr)
    except subprocess.CalledProcessError as e:
        print("Error during FFmpeg execution:")
        print(f"Return code: {e.returncode}")
        if e.stdout:
            print("FFmpeg stdout:")
            print(e.stdout)
        if e.stderr:
            print("FFmpeg stderr:")
            print(e.stderr)
    except FileNotFoundError:
        print("Error: ffmpeg command not found. Please ensure FFmpeg is installed and in your PATH.")

def main():
    """
    Main function to orchestrate the video creation process.
    Parses command-line arguments for input image and output video path.
    """
    parser = argparse.ArgumentParser(description="Create a video from a single image using FFmpeg.")
    parser.add_argument("input_image", help="Path to the input image file.")
    parser.add_argument("-o", "--output", help="Path to the output video file. Defaults to <input_image_name>.mp4.")

    args = parser.parse_args()

    input_image_path = args.input_image

    if args.output:
        output_video_path = args.output
    else:
        output_video_path = os.path.splitext(input_image_path)[0] + ".mp4"

    if not os.path.exists(input_image_path):
        print(f"Error: Input image '{input_image_path}' not found.")
        return

    create_video_from_image(input_image_path, output_video_path)

if __name__ == "__main__":
    main()
