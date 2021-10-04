import datetime
from time import time
from pygame import mixer


def play_music(file, I):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == I:
            mixer.music.stop()
            break


def file_open(action):
    with open("AbhishekHealth.txt", "a") as b:
        b.write(f"->> {action} :[ {datetime.datetime.now()} ] \n")


# timing log
work_start_time = "22:00:00"
work_end_time = "23:00:00"



def Main_Function():
    # Water drinking limits
    water_limit = 3500
    one_time_drink = 200
    no_of_glass = round(water_limit / one_time_drink)
    total_working_time =  8 * 60 * 60
    water_gap_time = round(total_working_time / no_of_glass)
    water_mp3 = "Drinkwater.mp3"
    water_start = time()

    # Eye exercises logs
    eye_exercise_gap_time = 30 * 60
    eye_mp3 = "eyeExe.mp3"
    eye_start = time()

    # Body exercises logs
    body_exercise_gap_time = 45 * 60
    body_start = time()
    body_mp3 = "bodyExe.mp3"

    while True:
        if time() - water_start > water_gap_time:
            print(f"Water drink time. if you drank type drank\n = ")
            play_music(water_mp3, "drank")
            file_open("Water Drank")
            water_start = time()
        if time() - eye_start > eye_exercise_gap_time:
            print(f"Eye Exercise time. if you complete type done\n = ")
            play_music(eye_mp3, "done")
            file_open("Eye Exercise Complete")
        if time() - body_start > body_exercise_gap_time:
            print(f"Body Exercise time. if you complete type doneby\n = ")
            play_music(body_mp3, "doneby")
            file_open("Eye Exercise Complete")


Main_Function()


