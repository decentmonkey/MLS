label college_computer:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Computer"
    return

label college_computer_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Coridor7", {"type":3, "text" : t_("КОМПЬЮТЕРНЫЙ КЛАСС"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_computer_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_computer")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_computer_environment:
    if obj_name == "Teleport_Coridor7":
        call change_scene("college_coridor7")
        return
    return
