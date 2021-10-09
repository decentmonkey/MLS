default collegeStudent19_Suffix = 1

label college_coridor9:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_9
    $ scene_image = "scene_COLLEGE_Coridor_9_base"
    return

label college_coridor9_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Student19", {"type" : 2, "base" : "COLLEGE_Coridor_9_Student19_[collegeStudent19_Suffix]", "click" : "college_coridor9_environment", "actions" : "l", "zorder":5, "selectable": False, "group":"students"}, scene="college_coridor9")

    $ add_object_to_scene("Teleport_Coridor10", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Coridor_9_Teleport_Coridor10", "click" : "college_coridor9_environment", "xpos" : 1657, "ypos" : 845, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor9")
    $ add_object_to_scene("Teleport_Teachers", {"type":3, "text" : t_("УЧИТЕЛЬСКАЯ"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_9_Teleport_Teachers", "click" : "college_coridor9_environment", "xpos" : 1010, "ypos" : 555, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor9")
    $ add_object_to_scene("Teleport_Library", {"type":3, "text" : t_("БИБЛИОТЕКА"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_9_Teleport_Library", "click" : "college_coridor9_environment", "xpos" : 396, "ypos" : 289, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor9")
    $ add_object_to_scene("Teleport_Coridor8", {"type":3, "text" : t_("ПРИЕМНАЯ ДИРЕКТОРА"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_9_Teleport_Coridor8", "click" : "college_coridor9_environment", "xpos" : 591, "ypos" : 930, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover":True}, scene="college_coridor9")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor9_environment:
    if obj_name == "Teleport_Coridor10":
        call change_scene("college_coridor10") from _rcall_change_scene_57
        return
    if obj_name == "Teleport_Teachers":
        call change_scene("college_teachers") from _rcall_change_scene_58
        return
    if obj_name == "Teleport_Library":
        call change_scene("college_library") from _rcall_change_scene_59
        return
    if obj_name == "Teleport_Coridor8":
        call change_scene("college_coridor8") from _rcall_change_scene_60
        return
    return
