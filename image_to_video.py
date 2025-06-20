import subprocess
import argparse
import os

def create_video_from_image(image_path, video_path):
    """
    Creates a video from a single image using FFmpeg.

    Args:
        image_path (str): The path to the input image.
        video_path (str): The path for the output video.
    """
    if not os.path.exists(image_path):
        print(f"Error: Input image not found at {image_path}")
        return

    # Overwrite output file if it exists
    if os.path.exists(video_path):
        print(f"Warning: Output file {video_path} already exists and will be overwritten.")

    ffmpeg_command = [
        'ffmpeg',
        '-y', # Overwrite output files without asking
        '-loop', '1',
        '-i', image_path,
        '-f', 'lavfi',
        '-i', 'anullsrc', # Generate a silent audio track
        '-c:v', 'libx264',
        '-t', '5', # Duration of the video
        '-vf', "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
        '-c:a', 'aac', # Audio codec
        '-shortest', # Finish encoding when the shortest input stream ends (audio in this case)
        video_path
    ]

    try:
        print(f"Executing FFmpeg command: {' '.join(ffmpeg_command)}")
        # Using PIPE for stdout and stderr to capture FFmpeg's output
        process = subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
        print("FFmpeg command executed successfully.")
        # FFmpeg often outputs informational messages to stderr, so we print both
        if process.stdout:
            print("FFmpeg stdout:\n", process.stdout)
        if process.stderr:
            print("FFmpeg stderr:\n", process.stderr)
        print(f"Video created successfully: {video_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during FFmpeg execution:")
        print(f"Command: {' '.join(e.cmd)}")
        print(f"Return code: {e.returncode}")
        if e.stdout:
            print(f"Stdout: {e.stdout}")
        if e.stderr:
            print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print("Error: FFmpeg not found. Please ensure FFmpeg is installed and in your system's PATH.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a video from an image using FFmpeg.")
    parser.add_argument("input_image", help="Path to the input image file.")
    parser.add_argument("output_video", help="Path to save the output video file.")

    args = parser.parse_args()

    create_video_from_image(args.input_image, args.output_video)
