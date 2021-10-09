label college_roof:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_14
    $ scene_image = "scene_COLLEGE_Roof"
    return

label college_roof_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor10", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Roof_Teleport_Coridor10", "click" : "college_roof_environment", "xpos" : 1123, "ypos" : 222, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_roof")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_roof_environment:
    if obj_name == "Teleport_Coridor10":
        call change_scene("college_coridor10") from _rcall_change_scene_75
        return
    return
