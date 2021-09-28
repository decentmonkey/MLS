label college_streetyard:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "scene_COLLEGE_StreetYard"
    return

label college_streetyard_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("КОЛЛЕДЖ"), "rarrow" : "arrow_up_2", "base":"COLLEGE_StreetYard_Teleport_Street", "click" : "college_streetyard_environment", "xpos" : 1542, "ypos" : 420, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_streetyard")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_streetyard_environment:
    if obj_name == "Teleport_Street":
        call change_scene("college_street")
        return
    return
