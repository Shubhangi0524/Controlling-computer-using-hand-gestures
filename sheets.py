import cv2
import numpy as np
from keras.models import load_model
import os
import sys
import pyttsx3

filepath = sys.argv[0]

REV_CLASS_MAP = {
     0 : 'cross',
     1 : 'down',
     2 : 'fist',
     3 : 'left',
     4 : 'none',
     5 : 'palm',
     6 : 'right',
     7 : 'scissor',
     8 : 'up',
     9 : 'y'
}


def mapper(val):
    return REV_CLASS_MAP[val]


model = load_model("C:\\Users\\sjkadam\\MY_FINAL_PROJECT\\handgesturemodel.h5")

# prepare the image
img = cv2.imread("C:\\Users\\sjkadam\\MY_FINAL_PROJECT\\MyImages\\valid\\y\\y10.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (224, 224))

# predict the move made
pred = model.predict(np.array([img]))
move_code = np.argmax(pred[0])
move_name = mapper(move_code)

print("Predicted: {}".format(move_name))

engine = pyttsx3.init()
# convert this text to speech
text = "Greetings of the day!"
text1 = "As gesture detected, opening the powerpoint"
text2 = "As gesture detected, opening the WhatsApp"
text3 = "As gesture detected, opening the Notepad++"
text4 = "As gesture detected, opening the Google Chrome"
text5 = "As gesture detected, opening the paint"
text6 = "As gesture detected, opening the acrobat document reader"
engine.say(text)
# play the speech
engine.runAndWait()


def play(gesture):
     if gesture == "scissor":
          os.startfile("C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE")
          engine.say(text1)

     elif gesture == "right":
          os.startfile("C:\\Users\\sjkadam\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
          engine.say(text2)

     elif gesture == "palm":
          os.startfile("C:\\Program Files (x86)\\Notepad++\\notepad++.exe")
          engine.say(text3)

     elif gesture == "y":
          os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
          engine.say(text4)

     elif gesture == "fist":
          os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")
          engine.say(text5)

     elif gesture == "down":
          os.startfile("C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe")
          engine.say(text6)


     engine.runAndWait()


kernel = np.ones((5, 5), np.uint8)



cap = cv2.VideoCapture(0)

prev_move = None

FONT = cv2.FONT_HERSHEY_SIMPLEX

while True:
     ret, frame = cap.read()
     if not ret:
          continue

     frame = cv2.flip(frame, 1)

     cv2.rectangle(frame, (300, 50), (600, 350), (255, 255, 255), 2)

     # extract the region of image within the user rectangle
     roi = frame[50:350, 300:600]
     img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
     img = cv2.resize(img, (224, 224))

     # predict the move made
     prediction = model.predict(np.array([img]))
     gesture_code = np.argmax(prediction[0])
     user_gesture = mapper(gesture_code)
     play(user_gesture)

     if user_gesture == "scissor":
          cv2.putText(frame, "Opening Powerpoint", (5, 50), FONT, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
          engine.say(text1)

     if user_gesture == "palm":
          cv2.putText(frame, "Opening Notepad++", (5, 50), FONT, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
          engine.say(text3)

     elif user_gesture == "right":
          cv2.putText(frame, "Opening Whatsapp", (5, 50), FONT, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
          engine.say(text2)

     elif user_gesture == "y":
          cv2.putText(frame, "Opening Google Chrome", (5, 50), FONT, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
          engine.say(text4)

     elif user_gesture == "fist":
          cv2.putText(frame, "Opening Paint", (5, 50), FONT, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
          engine.say(text5)

     elif user_gesture == "down":
          cv2.putText(frame, "Opening Acrobat Reader", (5, 50), FONT, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
          engine.say(text6)

     cv2.imshow("frame", frame)

     k = cv2.waitKey(10)
     if k == ord('q'):
          break
engine.runAndWait()
cap.release()
cv2.destroyAllWindows()
