label college_pool:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Pool"
    return

label college_pool_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor4", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_down_2", "base":"COLLEGE_Pool_Teleport_Coridor4", "click" : "college_pool_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_pool")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_pool_environment:
    if obj_name == "Teleport_Coridor4":
        call change_scene("college_coridor4")
        return
    return
