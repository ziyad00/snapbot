from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

# Replace the filename below.
required_video_file_name = "hi.mp4"
video_file = VideoFileClip(required_video_file_name)



clip_length = 60

video_length = video_file.duration
clip = int(video_length//clip_length)
last_clip = video_length %clip_length
length = 0


def extract(num):
  global length
  for time in range(0,clip+num):
    starttime = length
    if clip+num ==time:
      endtime = length+last_clip
    else:
        endtime = length+clip_length
    ffmpeg_extract_subclip(required_video_file_name, starttime, endtime, targetname=str(time)+".mp4")
    length+=clip_length

if video_length %clip_length !=0:
  extract(1)
else:
  extract(0)
