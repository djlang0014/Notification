import time
from plyer import notification
import winsound
from pathlib import Path
import argparse
import sys
import random

#Each line in the input file should have a message(which will be in the body of the notification)

parser=argparse.ArgumentParser()
parser.add_argument("in_file", help = "Input File Path")
parser.add_argument("period", help="Minutes between notifications")
parser.add_argument("wav_file", help = "File Path for Wav file for notification sound")
parser.add_argument("repeat", help = "1 if you want the notifications to rerandomize and repeat until you cancel it, 0 if you want it to end after going through each notification once")
args=parser.parse_args()
input=Path(args.in_file)

try:
    input = input.open("r")
except:
    print("Invalid Input File")
    sys.exit(1)

currentLine = input.readline()

if currentLine == "":
    print("Input File does not contain messages")
    sys.exit(1)

Notifications = []

while currentLine != "":
    Notifications.append(currentLine)
    currentLine = input.readline()

random.shuffle(Notifications)
StorageList = Notifications

while True:
    winsound.PlaySound(args.wav_file, winsound.SND_FILENAME)
    notification.notify(title = "Task Alert", message = StorageList.pop(), timeout = 60)
    
    if not len(StorageList) and args.repeat == "0":
        print("End of input file, program closing")
        break
    elif not len(StorageList):
        random.shuffle(Notifications)
        StorageList = Notifications
        print("Shuffled and starting over")

    time.sleep(60*(int(args.period)))

input.close()
sys.exit(0)

