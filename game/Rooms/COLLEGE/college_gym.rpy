label college_gym:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Gym"
    return

label college_gym_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor2", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Gym_Teleport_Coridor2", "click" : "college_gym_environment", "xpos" : 1343, "ypos" : 994, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_gym")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_gym_environment:
    if obj_name == "Teleport_Coridor2":
        call change_scene("college_coridor2") from _rcall_change_scene_64
        return
    return
