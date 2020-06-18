from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
import telebot


from telegram import Video


def myfunc():
  required_video_file_name = "hi.mp4"
  video_file = VideoFileClip(required_video_file_name)
  clip_length = 60
  video_length = video_file.duration
  clip = int(video_length//clip_length)
  last_clip = video_length %clip_length
  length = 0

  def extract(num):
    nonlocal length

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
TOEKN = "1092551482:AAGKHtbA_HDKTrTix2rK6_cfKbkk04R9Ys4"
bot = telebot.TeleBot(TOEKN)


def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def videoHandler(message,update):
  print("Fffffffffff")
  raw = message.photo[-1].file_id
  print(raw)
  path = raw+".jpg"
  file_info = bot.get_file(raw)
  downloaded_file = bot.download_file(file_info.file_path)
  with open(path,'wb') as new_file:
    new_file.write(downloaded_file)
  #filee = bot.getFile(bot.message.photo[-1].file_id)
  #print(filee.file_path)
  #filee.download('video.mp4')

@bot.message_handler(content_types=['video', 'audio'])
def function_name(message):
  bot.reply_to(message, "This is a message handler")
  raw = message.video.file_id
  print(raw)
  path = raw+".mp4"
  file_info = bot.get_file(raw)
  downloaded_file = bot.download_file(file_info.file_path)
  with open(path,'wb') as new_file:
    new_file.write(downloaded_file)

bot.polling()

#updater = Updater(TOEKN, use_context=True)

#updater.dispatcher.add_handler(MessageHandler(Filters.photo, videoHandler))
#updater.dispatcher.add_handler(CommandHandler("hello", hello))

#updater.start_polling()
#updater.idle()