from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import telebot


numOfVideo = 0

TOKEN = "1092551482:AAGKHtbA_HDKTrTix2rK6_cfKbkk04R9Ys4"
bot = telebot.TeleBot(TOKEN)

def myfunc(name,numOfVideo):
  numofVideos = 0
  required_video_file_name = name
  video_file = VideoFileClip(required_video_file_name)
  clip_length = 59
  video_length = video_file.duration
  clip = int(video_length//clip_length)
  last_clip = video_length %clip_length
  length = 0
  if int(video_length) <= clip_length:
    return False
  def extract(num):
    nonlocal length
    for time in range(0,clip+num):
      starttime = length
      if clip+num ==time:
        endtime = length+last_clip
      else:
        endtime = length+clip_length

      ffmpeg_extract_subclip(required_video_file_name, starttime, endtime, targetname=str(time+numOfVideo)+".mp4")
      length+=clip_length

  if video_length %clip_length !=0:
    numofVideos = int(video_length//clip_length +1)

    extract(1)
  else:
    numofVideos = int(video_length//clip_length)
    extract(0)
  return numofVideos


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am SnapBot.
I am here to take your long video and send it to you as short videos to share it on SnapChat!.\
 Just send any long video and I'll do the rest!\
note: the size of the video should be less than 20 MB and the length should be more than 59 seconds.
""")




@bot.message_handler(content_types=['video'])
def function_name(message):
  try:
    global numOfVideo
    raw = message.video.file_id
    path = raw+".mp4"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(path,'wb') as new_file:
      new_file.write(downloaded_file)
    numOfVideos = myfunc(path,numOfVideo)
    if numOfVideos !=False:
      bot.reply_to(message, "on progress...")
      for i in range(numOfVideo, numOfVideo+numOfVideos):
        video = open(f'{i}.mp4', 'rb')
        bot.send_video(message.chat.id, video)
        #bot.send_video(message.chat.id, "FILEID")
      numOfVideo+=1
  except:
    pass

bot.polling()

