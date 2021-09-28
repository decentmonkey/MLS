label college_biology:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Biology"
    return

label college_biology_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor1", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Biology_Teleport_Coridor1", "click" : "college_biology_environment", "xpos" : 755, "ypos" : 106, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_biology")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_biology_environment:
    if obj_name == "Teleport_Coridor1":
        call change_scene("college_coridor1")
        return
    return
