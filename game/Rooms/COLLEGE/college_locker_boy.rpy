label college_locker_boy:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate()
    $ scene_image = "scene_COLLEGE_Locker_Boy"
    return

label college_locker_boy_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor4", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_locker_boy_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_locker_boy")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_locker_boy_environment:
    if obj_name == "Teleport_Coridor4":
        call change_scene("college_coridor4")
        return
    return
