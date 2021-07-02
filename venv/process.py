from pywinauto.application import Application
import time
import pywinauto
import pywinauto.keyboard as key
import speech_recognition as sr
import konlpy
from konlpy.tag import Mecab
import re
import os
import time
import winautoFunctions

def func():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        s=r.recognize_google(audio, language='ko-KR')
        print("You said: " + s)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return s



def matching(s):
    a = mecab.pos(s)
    dic_n={
        '크롬':'Chrome',
        '엣지':'Edge',
        '컴퓨터':'computer',
        '파이참':'PyCharm'
    }

    dic_o={
        '뒤':'back',
        '앞':'front',
        '꺼':'shut',
        '켜':'on',
        '검색':'search'
    }

    res = [' ',' ',' ']
    for i in a:
        print(i)
        if "NNG" in i[1]:
            if i[0] in dic_o:
                res[1] = dic_o[i[0]]
                continue
            if i[0] in dic_n:
                res[0] = dic_n[i[0]]
                continue

        if "VV" in i[1]:
            if i[0] in dic_o:
                res[1] = dic_o[i[0]]
                continue

        if "NN" == i[1]:
            if i[0] in dic:
                res[0] = dic[i[0]]
                continue

    return res

#
# title = 'Edge'
# for i in pywinauto.findwindows.find_elements():
#     if re.search('Edge',i.name) != None:
#         break;
#     if re.search('Chrome',i.name) != None:
#         title = 'Chrome'
#         break;
#
# app = Application(backend='uia')
# app.connect(title_re='.*'+title+'.*', found_index=0)
# window = app.top_window()
# window.set_focus()
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mecab\mecab-ko-dic")

try:
    mecab = Mecab(dicpath='C:\mecab\mecab-ko-dic')
except:
    mecab = Mecab(dicpath=path)


sta = time.time()
win,order,obj = matching(func())

while win != ' ' and order != ' ':

    if win == 'computer':
        if order == 'shut':
            winautoFunctions.close_all_window()
            winautoFunctions.shutdown_computer()

    if win != ' ' and win != 'computer':
        app.connect(title_re='.*' + win + '.*', found_index=0)
        window = app.top_window()
        window.set_focus()

    if order ==  'back':
        key.send_keys('%{LEFT}')
    if order == 'front':
        key.send_keys('%{RIGHT}')
    if order ==  'shut':
        key.send_keys('^w')
    if order ==  'on':
        key.send_keys('^t')
    if order == 'search':
        winautoFunctions.search_keyword(obj,window)


    print(time.time()-sta)

    win,order,obj = matching(func())

    sta = time.time()


