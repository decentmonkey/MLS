label college_geography:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Geography"
    return

label college_geography_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor3", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Geography_Teleport_Coridor3", "click" : "college_geography_environment", "xpos" : 230, "ypos" : 327, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_geography")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_geography_environment:
    if obj_name == "Teleport_Coridor3":
        call change_scene("college_coridor3")
        return
    return
