label college_library:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate()
    $ scene_image = "scene_COLLEGE_Library"
    return

label college_library_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor9", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "college_library_environment", "xpos" : 1581, "ypos" : 975, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_library")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_library_environment:
    if obj_name == "Teleport_Coridor9":
        call change_scene("college_coridor9")
        return
    return
