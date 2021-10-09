label college_teachers:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Teachers"
    return

label college_teachers_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor9", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Teachers_Teleport_Coridor9", "click" : "college_teachers_environment", "xpos" : 1568, "ypos" : 860, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_teachers")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_teachers_environment:
    if obj_name == "Teleport_Coridor9":
        call change_scene("college_coridor9") from _rcall_change_scene_79
        return
    return
