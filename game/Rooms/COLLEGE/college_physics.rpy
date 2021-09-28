label college_physics:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Physics"
    return

label college_physics_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor6", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "college_physics_environment", "xpos" : 1620, "ypos" : 993, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_physics")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_physics_environment:
    if obj_name == "Teleport_Coridor6":
        call change_scene("college_coridor6")
        return
    return
