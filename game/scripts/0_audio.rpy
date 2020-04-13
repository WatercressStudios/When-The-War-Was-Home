init python:
    #ambient sound effect channel
    renpy.music.register_channel("env", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)
