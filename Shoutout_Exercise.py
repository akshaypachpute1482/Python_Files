import win32com.client as win
l= ["Akshay", "Akshay", "Akshay", "Akshay",]
spk= win.Dispatch("SAPI.SpVoice")

for n in l:
    spk.Speak(f"{n}")

import pyttsx3 as py
l= ["Hello Akshay"]
f= py.init()
v=f.getProperty('voices')
f.setProperty('voice', v[1].id)
for k in l:
 f.say(l)
f.runAndWait()



import time
init = time.time()
print(init)

t1= time.time()- init
print(t1)

def gen():
   for i in range(2):
      yield i
g=gen()
print(next(g))     
print(next(g))
print(next(g))
print(next(g))