# Project :-  Healthy Programmer
# programmer works from 9am to 5pm
# for water reminder - play water mp3 (3.5 litres should be drank) - drank - log
# eyes - eyes mp3 play as a reminder (every 30 minutes) - eyedone - log
# physical activity - physical mp3 reminder - every 45 minutes - exercise done - log
# use pygame module to play the audio.

# solution:

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper): # file means that file which has music,stopper means that word which stops music.
    mixer.init()  # # this is the first step to start the mixer.
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")


