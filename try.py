# import tkinter as tk
# import pyautogui as coordinates

# win = tk.Tk()
# win.geometry('200x50+550+250')
# win.title('Mos Loc')
# win.config(bg='#323232')
# # win.attributes('-topmos', 1)

# frame = tk.Frame()


# lab = tk.Label(text='')
# lab.pack()


# def update():
#     lab.configure(text='this are your ' +str( coordinates.position()))
    
#     frame.after(20, update)


# update()
# frame.mainloop()

# python3
# import threading

# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
    
#     while True :
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    
#         while x > 300:
            
#             print(positionStr, end='')
#             print('\b' * len(positionStr), end='', flush=True)
#         while x < 300:
#             # x, y = pyautogui.position()
#             # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

#             def setInterval(func,time):
#                 e = threading.Event()
#                 while not e.wait(time):
#                     func()
#             def foo():
#                 print('you need to go back')
#             setInterval(foo,5)

#         # else:
#             # def setInterval(func,time):
#             #     e = threading.Event()
#             #     while not e.wait(time):
#             #         func()
#             # def foo():
#             #     print('you need to go back')
#             # setInterval(foo,5)
# except KeyboardInterrupt:
#     print('\n')

# Import the required module for text 
# # to speech conversion
# from gtts import gTTS

# # This module is imported so that we can 
# # play the converted audio
# import os

# # The text that you want to convert to audio
# mytext = 'Welcome to geeksforgeeks!'

# # Language in which you want to convert
# language = 'en'

# # Passing the text and language to the engine, 
# # here we have marked slow=False. Which tells 
# # the module that the converted audio should 
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
# # Saving the converted audio in a mp3 file named
# # welcome 
# myobj.save("welcome.mp3")

# # Playing the converted file
# os.system("mpg321 welcome.mp3")


from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
import time
# Create the text
text = "Hello World! This is How about a drink"
tts = gTTS(text, slow=False, pre_processor_funcs = [abbreviations, end_of_line]) 
# Save the audio in a mp3 file
tts.save('hello.mp3')
# Play the audio
mixer.init()
mixer.music.load("hello.mp3")
mixer.music.play()
# Wait for the audio to be played
time.sleep(2)

# from datetime import date

# today = date.today()
# print("Today's date:", today)

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")
print(dt_string)	