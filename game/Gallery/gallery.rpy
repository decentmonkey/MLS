label process_gallery(gallery_label):
    music stop
    img black_screen
    with diss
#    python:
#        storedRain = rain
#        rain = False
#        storedVar = {}
#        for key1 in dir():
#            if key1 != "storedVar":
#                try:
#                    storedVar[key1] = globals()[key1]
#                except TypeError:
#                    pass
    pause 0.5
    call expression gallery_label
    hide screen photoshoot_camera_icon
    hide screen photoshoot
#    python:
#        rain = storedRain
#        for key1 in storedVar:
#            globals()[key1] = storedVar[key1]
#        storedVar = False

    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_29
    return
