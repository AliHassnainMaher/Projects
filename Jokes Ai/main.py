import pyjokes
import gtts
import playsound
import os
def joke():
    joke = pyjokes.get_joke()
    tts = gtts.gTTS(joke)
    tts.save('joke.mp3')
    print(joke)
    playsound.playsound('joke.mp3')
    os.remove('joke.mp3')
while True:
    joke()
    _joke = input("Do you want to hear another joke? (y/n): ")
    if _joke == 'y':
        joke()
    else:
        break
