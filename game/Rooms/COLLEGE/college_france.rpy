label college_france:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_France"
    return

label college_france_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2_a", "base":"COLLEGE_France_Teleport_Coridor", "click" : "college_france_environment", "xpos" : 402, "ypos" : 321, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_france")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_france_environment:
    if obj_name == "Teleport_Coridor":
        call change_scene("college_coridor1") from _rcall_change_scene_62
        return
    return
