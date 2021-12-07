label college_hall:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Hall"
    return

label college_hall_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor1", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Hall_Teleport_Coridor1", "click" : "college_hall_environment", "xpos" : 1601, "ypos" : 904, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_hall")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_hall_environment:
    if obj_name == "Teleport_Coridor1":
        call change_scene("college_coridor1") from _rcall_change_scene_65
        return
    return
