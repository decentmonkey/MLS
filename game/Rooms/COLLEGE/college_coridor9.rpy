label college_coridor9:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Coridor_9_base"
    return

label college_coridor9_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "college_coridor9_environment", "actions" : "l", "zorder":10}, scene="college_coridor9")

    $ add_object_to_scene("Teleport_Coridor10", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_9_Teleport_Coridor10", "click" : "college_coridor9_environment", "xpos" : 1657, "ypos" : 845, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor9")
    $ add_object_to_scene("Teleport_Teachers", {"type":3, "text" : t_("УЧИТЕЛЬСКАЯ"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_9_Teleport_Teachers", "click" : "college_coridor9_environment", "xpos" : 1010, "ypos" : 555, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor9")
    $ add_object_to_scene("Teleport_Library", {"type":3, "text" : t_("БИБЛИОТЕКА"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_9_Teleport_Library", "click" : "college_coridor9_environment", "xpos" : 396, "ypos" : 339, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor9")
    $ add_object_to_scene("Teleport_Coridor8", {"type":3, "text" : t_("ПРИЕМНАЯ ДИРЕКТОРА"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_9_Teleport_Coridor8", "click" : "college_coridor9_environment", "xpos" : 591, "ypos" : 930, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor9")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor9_environment:
    if obj_name == "Teleport_Coridor10":
        call change_scene("college_coridor10")
        return
    if obj_name == "Teleport_Teachers":
        call change_scene("college_teachers")
        return
    if obj_name == "Teleport_Library":
        call change_scene("college_library")
        return
    if obj_name == "Teleport_Coridor8":
        call change_scene("college_coridor8")
        return
    return
