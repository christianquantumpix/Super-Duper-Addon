import aud
#import bpy
import os
import random

def play_sound(category):
    gutsche = "gutsche"
    brachert = "brachert"

    path = os.path.dirname(os.path.abspath(__file__))

    suffix = "/brachert"

    if gutsche in path:
        suffix = "/gutsche"
    elif brachert in path: 
        suffix = "/brachert"

    audio_path = path + "/audio" + suffix + "/" + category
    audio_files = os.listdir(audio_path)

    print(audio_path)
    print(audio_files)

    random_index = random.randrange(0, len(audio_files))
    print(random_index)

    device = aud.Device()
    sound = aud.Sound(audio_path + "/" + audio_files[random_index])
    handle = device.play(sound)