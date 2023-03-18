from gtts import gTTS
import random
import os
from mutagen.mp3 import MP3
import cv2
import datetime
from moviepy.editor import *
import datetime
import time
import subprocess
import openai
import re
###
##
####import Config
####import Reddit
####import Thought
##openai.api_key =("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")
## 
###from googleclientapi.http import MediaFileUpload
###from google_apis import create_service
##
##def audio_duration(length):
##    hours = length // 3600 
##    length %= 3600
##    mins = length // 60 
##    length %= 60
##    seconds = length
##    return hours, mins, seconds
##
##language = 'en'
##
##
##response = openai.Completion.create(
##  model="text-davinci-003",
##  prompt="write me a list of 4 shower thoughts",
##  temperature=0.7,
##  max_tokens=256,
##  top_p=1,
##  frequency_penalty=0,
##  presence_penalty=0
##)
##
##js = response["choices"][0]["text"]
##text = re.split("\n\n1. |\n2. |\n3. |\n4. |\n5. ",js)
##del text[0]
##
##text[1] = "Shower Thoughts.  "
##text = str(text)
##print ("The Following text will be turned into a video : " + text)
##
##
##
##subprocess.run(["py","C:/Users/Student/Downloads/youtubepython/tiktokttstest.py","-v","en_male_cody","-n","C:/Users/Student/Downloads/youtubepython/audio.mp3","-t",text,"--session","e75e33436d4fcb9293939ac597356a77"])
##
##
##
###vidchoice = int(input("Select background, 1 for Minecraft, 2 for Geometry Dash"))
##
##vidchoice = 1
##
##if vidchoice == 1:
##    audio = MP3("audio.mp3")
##    ttstime = audio.info.length
##    print("length of tts: " + str(ttstime))
##    data = cv2.VideoCapture("minecraft.mp4")
##    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
##    fps = data.get(cv2.CAP_PROP_FPS)
##    seconds = round(frames / fps)
##    video_time = datetime.timedelta(seconds=seconds)
##    print(f"video time in seconds: {seconds}")
##    if int(ttstime) >= int(seconds):
##        print("tts too long!")
##    else:
##        print("audio is compatible with video, continuing to editing process")
##        clip = VideoFileClip("minecraft.mp4")
##        clip = clip.subclip(0, ttstime)
##        audioclip = AudioFileClip("audio.mp3")
##        videoclip = clip.set_audio(audioclip)
##        videoclip.write_videofile('short.mp4', threads = 8, fps=24)
#####      

    













import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import openai
import re
import pyautogui
openai.api_key =("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")

previdname = openai.Completion.create(
  model="text-davinci-003",
  prompt="create a original, viral, funny title for a YouTube shorts video about shower thoughts",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

oldvidname = previdname["choices"][0]["text"]
vidname = re.split("\n\n",oldvidname)
print("video name = " + str(vidname))
options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("user-data-dir=C:\\Users\\Student\\AppData\\Local\\Google\\Chrome Beta\\User")
options.binary_location = "chromedriver.exe"
print("\033[1;31;40m IMPORTANT: Put one or more videos in the *videos* folder in the bot directory. Please make sure to name the video files like this --> Ex: vid1.mp4 vid2.mp4 vid3.mp4 etc..")
print("\033[1;32;40m Press 1 if you want to spam same video or Press 2 if you want to upload multiple videos: ")
answer = 1
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
if(int(answer) == 1):
    #nameofvid = input("\033[1;33;40m Put the name of the video you want to upload (Ex: vid.mp4 or myshort.mp4 etc..) ---> ")
    howmany = input("\033[1;33;40m How many times you want to upload this video ---> ")
    nameofvid = r"C:\Users\Student\Downloads\youtubepython\short.mp4"
    
    for i in range(int(howmany)):

        vidname = openai.Completion.create(
          model="text-davinci-003",
          prompt="create a original, viral, funny title for a YouTube shorts video about shower thoughts",
          temperature=0.7,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        
        oldvidname = previdname["choices"][0]["text"]
        vidname = re.split("\n\n",oldvidname)
        del vidname[0]
        #making the video
        def audio_duration(length):
            hours = length // 3600 
            length %= 3600
            mins = length // 60 
            length %= 60
            seconds = length
            return hours, mins, seconds

        language = 'en'


        response = openai.Completion.create(
          model="text-davinci-003",
          prompt="write me a list of 4 shower thoughts",
          temperature=0.7,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )

        js = response["choices"][0]["text"]
        text = re.split("\n\n1. |\n2. |\n3. |\n4. |\n5. ",js)
        del text[0]

        text[1] = "Shower Thoughts.  "
        text = str(text)
        print ("The Following text will be turned into a video : " + text)



        subprocess.run(["py","C:/Users/Student/Downloads/youtubepython/tiktokttstest.py","-v","en_male_cody","-n","C:/Users/Student/Downloads/youtubepython/audio.mp3","-t",text,"--session","e75e33436d4fcb9293939ac597356a77"])



        #vidchoice = int(input("Select background, 1 for Minecraft, 2 for Geometry Dash"))

        vidchoice = 1

        if vidchoice == 1:
            audio = MP3("audio.mp3")
            ttstime = audio.info.length
            print("length of tts: " + str(ttstime))
            data = cv2.VideoCapture("minecraft.mp4")
            frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
            fps = data.get(cv2.CAP_PROP_FPS)
            seconds = round(frames / fps)
            video_time = datetime.timedelta(seconds=seconds)
            print(f"video time in seconds: {seconds}")
            if int(ttstime) >= int(seconds):
                print("tts too long!")
            else:
                print("audio is compatible with video, continuing to editing process")
                clip = VideoFileClip("minecraft.mp4")
                clip = clip.subclip(0, ttstime)
                audioclip = AudioFileClip("audio.mp3")
                videoclip = clip.set_audio(audioclip)
                videoclip.write_videofile('short.mp4', threads = 8, fps=24)
        #uploading video
        bot = uc.Chrome()
        bot.get("https://studio.youtube.com")
        time.sleep(3)
        uname = bot.find_element('xpath', '//input[@type="email"]')
        uname.send_keys("doasdasus@gmail.com")
        time.sleep(1)
        uname.send_keys(Keys.RETURN)
        time.sleep(3)
        uname = bot.find_element('xpath', '//input[@type="password"]')
        uname.send_keys("144160156")
        time.sleep(1)
        uname.send_keys(Keys.RETURN)
        
        time.sleep(3)
        
        upload_button = bot.find_element('xpath', '//*[@id="upload-icon"]')
        upload_button.click()
        time.sleep(1)

        file_input = bot.find_element('xpath', '//*[@id="content"]/input')
        simp_path = 'videos/{}'.format(str(nameofvid))
        
        abs_path = os.path.abspath(r"C:\Users\Student\Downloads\youtubepython\short.mp4")
        file_input.send_keys(abs_path)

        time.sleep(7)
        pyautogui.typewrite(str(vidname))

        
        time.sleep(1)
        
        kids = bot.find_element('xpath', '//*[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]')
        for i in range(3):
            kids.click()
            time.sleep(1)

        next_button = bot.find_element('xpath', '//*[@id="next-button"]')
        for i in range(3):
            next_button.click()
            time.sleep(1)

        publish = bot.find_element('xpath', '//*[@name="PUBLIC"]')
        publish.click()
        time.sleep(2)
        
        done_button = bot.find_element('xpath', '//*[@id="done-button"]')
        done_button.click()
        time.sleep(5)
        bot.quit()






