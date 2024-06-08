import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip
import numpy as np

def create_video(text):
    user_text = text
    video_duration = 3
    fps = 24
    video_width = 100
    video_height = 100
    text_size = 50
    text_color = ['white', 'red', 'green', 'blue']
    background_color = (0, 0, 0)

    font_path = "DejaVuSerif-Bold.ttf"
    font = ImageFont.truetype(font_path, text_size)

    text_bbox = font.getbbox(user_text)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    total_frames = video_duration * fps

    frames = []
    for i in range(total_frames):
        img = Image.new('RGB', (video_width, video_height), color=background_color)
        draw = ImageDraw.Draw(img)
        x_position = video_width - int(i * (video_width + text_width) / total_frames)
        draw.text((x_position, (video_height - text_height) // 2), user_text, font=font, fill=text_color[i%4])
        frames.append(np.array(img))

    clip = ImageSequenceClip(frames, fps=fps)
    video_path = "runner.mp4"

    clip.write_videofile(video_path, fps=24)
    
    return video_path