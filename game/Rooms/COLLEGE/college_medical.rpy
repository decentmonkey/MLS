label college_medical:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Medical"
    return

label college_medical_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor2", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_medical_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_medical")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_medical_environment:
    if obj_name == "Teleport_Coridor2":
        call change_scene("college_coridor2")
        return
    return
