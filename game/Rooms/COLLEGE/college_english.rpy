label college_english:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_English"
    return

label college_english_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "college_english_environment", "actions" : "l", "zorder":10}, scene="college_english")

    $ add_object_to_scene("Teleport_Coridor6", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_down_2_a", "base":"COLLEGE_English_Teleport_Coridor6", "click" : "college_english_environment", "xpos" : 426, "ypos" : 248, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_english")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_english_environment:
    if obj_name == "Teleport_Coridor6":
        call change_scene("college_coridor6")
        return
    return
