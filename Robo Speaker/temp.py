from playsound import playsound
from gtts import gTTS

def user_speech():
    print("I Am A Robot Speaker Made By Ali Hassnain")
    user_want_to_speak = input("Enter What You Want To Speak: ")
    tts = gTTS(user_want_to_speak)
    tts.save('user.mp3')
    playsound('user.mp3')
    return user_want_to_speak  # Return the user's input to save later if needed.

# Call user_speech function
user_input = user_speech()

recall_request = input("Do You Want To Speak Any More (yes/no): ").lower()
user_write_data = input("Do You Want To Save Your Conversation (yes/no): ").lower()

# Process the user's responses
if recall_request == "yes":
    user_input += '\n' + user_speech()  # Append new speech to previous input.
elif user_write_data == "yes":
        with open("data\main.conversation.txt", "w") as f:
        f.write(user_input)  #Saving The File 
else:
    print("Thanks For Using Me.")
#for some fun
print("saving...")

