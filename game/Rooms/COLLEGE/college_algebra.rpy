label college_algebra:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Algebra"
    return

label college_algebra_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor5", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Algebra_Teleport_Coridor5", "click" : "college_algebra_environment", "xpos" : 436, "ypos" : 314, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_algebra")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_algebra_environment:
    if obj_name == "Teleport_Coridor5":
        call change_scene("college_coridor5") from _rcall_change_scene_19
        return
    return
