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


# from gtts import gTTS
# from gtts.tokenizer.pre_processors import abbreviations, end_of_line
# from pygame import mixer
# import time
# # Create the text
# text = "Hello World! This is How about a drink"
# tts = gTTS(text, slow=False, pre_processor_funcs = [abbreviations, end_of_line]) 
# # Save the audio in a mp3 file
# tts.save('hello.mp3')
# # Play the audio
# mixer.init()
# mixer.music.load("hello.mp3")
# mixer.music.play()
# # Wait for the audio to be played
# time.sleep(2)

# # from datetime import date

# # today = date.today()
# # print("Today's date:", today)

# from datetime import datetime

# # datetime object containing current date and time
# now = datetime.now()
 
# print("now =", now)

# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")
# print(dt_string)	


# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'timeConversion' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.
# #

# def timeConversion(s):
#     lstr=list(s)
#     print('s is:',lstr)
#     AMPM = s[-2:]
#     print('AMPM:',AMPM)
#     print('first 2 of s:',s[0:2])

#     if AMPM == 'AM':

#         if s[0:2]=='12':
#             print('thisss')
#             print(lstr[0:2])

#             lstr[0]='0'
#             lstr[1]='0'
        
#             print('this strzzz:',lstr[0:-2])
#         else:
#             print('this strzzz:',lstr[0:-2])
#     if AMPM == 'PM':

#         if s[0:2]=='12':
#             lstr[0]='1'
#             lstr[1]='2'
        
#             print('this strzzz:',lstr[0:-2])
#         else:
#             lstr[0]=str(int(lstr[0])+1)
#             lstr[1]=str(int(lstr[1])+2)
#             print('this strzzz:',lstr[0:-2])

#     print(''.join(lstr[0:-2]))
#     return(''.join(lstr[0:-2]))
#             # output =  
#     # print('this s:',str)
#     # Write your code here
# timeConversion( '02:01:00AM')


import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

# ---------------------------------------------------------------------------------
# queries = ['ab','abc','bc']
# strings = ['ab','ab','abc']

# def matchingStrings(strings, queries):

#     outlist=[]
#     for que in queries:
#         count = 0
#         for str in strings:
#             if que == str:
#                 count = count + 1
#         outlist.append(count)
#     print('outlist:', outlist)
        
#     # Write your code here

# matchingStrings(strings, queries)
# -------------------------------------------------------------------
# n =9
# # print(bin(n))

# print('{:032b}'.format(n))

# def flippingBits(n):
#     # print('n is:',n)
#     binry = '{:032b}'.format(n)
#     lbinry = list(binry)
#     # lbinry[0]='z'
#     print('this lbinry:',lbinry)
#     print('length binary:',len(lbinry))
#     for x in range(len(lbinry)):
#         print('this x:',x)
#         print(lbinry[x])
#         print(type(lbinry[x]))
#         if lbinry[x]=='0':
#             print('fulfiiled')
#             print(lbinry[x])
#             lbinry[x] = 1
#         if lbinry[x]=='1':
#             lbinry[x] = 0
#     outnum=''
#     for lbin in lbinry:
#         outnum = outnum + str(lbin)
#     output = int(outnum,2)
#     print('output:',output)
#     return output

#     # Write your code here
# flippingBits(n)
list = [0,9,1,2,3,3]
list.sort()
print(list)
# print([0,9,1,2,3,3].sort())
def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for x in range(len(A)):
        if A[x] + B[x] >= k:
            continue
        return 'NO'
    return 'YES'

A=[0,1]
B=[0,2]
k=1
print(twoArrays(k,A,B))


    # print(k,A,B)
