
import aud
import bpy
import os
import random

from time import sleep
from threading import Timer

from random import randint

class ModalOperator(bpy.types.Operator):
    bl_idname = "object.modal_operator"
    bl_label = "Super Duper Addon"

    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")

    def execute(self, context):
        return {'FINISHED'}

    def modal(self, context, event):
        print(event.type)
        if (event.type == 'C' and event.ctrl and event.value == 'RELEASE') or (event.type == 'D' and event.shift and event.value == 'RELEASE'):
            if random.random() > 0.33:
                play_sound('copy')
            return {'PASS_THROUGH'}
        elif (event.type == 'DEL' or event.type == 'BACK_SPACE') and event.value == 'RELEASE':
            if random.random() > 0.33:
                play_sound('delete')
                return {'PASS_THROUGH'}
        elif event.type == 'S' and event.ctrl and event.value == 'PRESS':
            if random.random() > 0:
                play_sound('save')
                return {'PASS_THROUGH'}
        elif event.value == 'RELEASE':
            if random.random() > 0.75:
                play_sound('generic')
                return {'PASS_THROUGH'}
        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        #self.execute(context)

        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

# Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(ModalOperator.bl_idname, text="Super Duper Addon")

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

bl_info = {
    "name": "Super Duper Addon",
    "author": "Christian Simon",
    "version": (0, 0, 1),
    "blender": (3, 3, 1),
    "category": "System",
}

def register():
    # Register and add to the object menu (required to also use F3 search "Modal Operator" for quick access).
    bpy.utils.register_class(ModalOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    # bpy.path module should have similar scope but results in errors somehow. 
    gutsche = "gutsche"
    brachert = "brachert"

    path = os.path.dirname(os.path.abspath(__file__))

    suffix = "/brachert"

    if gutsche in path:
        suffix = "/gutsche"
    elif brachert in path: 
        suffix = "/brachert"

    audio_path = path + "/audio" + suffix + "/welcome"

    audio_files = os.listdir(audio_path)
    print(audio_files)

    device = aud.Device()

    random_index = random.randrange(0, len(audio_files))

    sound = aud.Sound(audio_path + '/' + audio_files[random_index])
    handle = device.play(sound)
    
def unregister():
    bpy.utils.unregister_class(ModalOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
