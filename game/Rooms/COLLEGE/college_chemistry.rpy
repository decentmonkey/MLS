label college_chemistry:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Chemistry"
    return

label college_chemistry_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor2", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "college_chemistry_environment", "xpos" : 287, "ypos" : 979, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_chemistry")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_chemistry_environment:
    if obj_name == "Teleport_Coridor2":
        call change_scene("college_coridor2") from _rcall_change_scene_22
        return
    return
