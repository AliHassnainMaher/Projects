from playsound import playsound
from gtts import gTTS
import os
#import pyttsx3
'''
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
'''
def user_speech():
    print("I Am A Robot Speaker Made By Ali Hassnain")
    user_want_to_speak = input("Enter What You Want To Speak: ")
    tts = gTTS(user_want_to_speak)
    tts.save('user.mp3')
    playsound('user.mp3')
    return user_want_to_speak

# Initialize counter and file
if not os.path.exists("data"):
    os.makedirs("data")  

file_path = "data/main.conversation.txt"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    count = len(lines) + 1 
else:
    count = 1  


user_input = user_speech()

recall_request = input("Do You Want To Speak Any More (yes/no): ").lower()
if recall_request == "yes":
    user_input += '\n' + user_speech()

user_write_data = input("Do You Want To Save Your Conversation (yes/no): ").lower()

if user_write_data == "yes":
    with open(file_path, "a") as f:
        for line in user_input.split('\n'):
            f.write(f"{count}: {line}\n")  
            count += 1
else:
    print("Thanks For Using Me.")
# for some fun
print("saving...")
