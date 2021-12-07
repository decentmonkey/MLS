label college_streetyard:
    $ miniMapData = []
    if ep1_college_minimap_enabled == True:
        call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_16
    $ sceneIsStreet = True
    $ scene_image = "scene_COLLEGE_StreetYard[day_suffix]"
    if day_time_idx == 3:
        $ scene_image = "scene_COLLEGE_StreetYard_Night"
    return

label college_streetyard_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("КОЛЛЕДЖ"), "rarrow" : "arrow_up_2", "base":"empty", "click" : "college_streetyard_environment", "xpos" : 1542, "ypos" : 420, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_streetyard")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_streetyard_environment:
    if obj_name == "Teleport_Street":
        call change_scene("college_street") from _rcall_change_scene_78
        return
    return
