import os
from moviepy.editor import VideoFileClip
from moviepy.editor import ImageSequenceClip
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.editor import *
from natsort import natsorted

INPUT_DIR = "gifs"
OUTPUT_DIR = "output"

# Create output directory if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# List and sort all gif files
all_files = os.listdir(INPUT_DIR)
gif_files = natsorted([f for f in all_files if f.lower().endswith(".gif")])

if not gif_files:
    print("No GIF files found in the input directory.")
    exit(1)

# Convert each GIF to MP4
for gif_file in gif_files:
    gif_path = os.path.join(INPUT_DIR, gif_file)
    output_filename = os.path.splitext(gif_file)[0] + ".mp4"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    print(f"Converting {gif_file} -> {output_filename} ...")

    try:
        clip = VideoFileClip(gif_path)
        clip.write_videofile(output_path, codec="libx264", audio=False)
        clip.close()
    except Exception as e:
        print(f"Error converting {gif_file}: {e}")

print("All GIFs have been converted.")
