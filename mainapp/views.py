
from django.shortcuts import render, redirect, HttpResponse
from gtts import gTTS
import string
import random
import os
import shutil



def index_page(request):
    print("hi")
    if request.method == "POST":
        # letters = string.ascii_lowercase

        # file_name = f"{''.join(random.choice(letters) for i in range(10))}.mp3"

        text = request.POST['text']
        tdl = request.POST['tdl']
        lang = request.POST['lang']

        tts = gTTS(text, lang=lang, tld=tdl)
        # tts.save(file_name)
        tts.save('okay.mp3')

        os.system("mpg321 okay.mp3")
        # dir = os.getcwd()
        # full_dir = os.path.join(dir, file_name)
    
        # print(dir)
        # print(full_dir)

        # dest = shutil.move(full_dir, os.path.join(
            # dir, "mainapp/static/sound_file"))

        # data = {"loc" :file_name}
        # return render(request,'download.html',data)
    
        return render(request, 'index.html', {'loc':text})
    return render(request, 'index.html', {'loc':text})
    # return None
    
