default collegeStudent18_Suffix = 1

label college_coridor8:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_8
    $ scene_image = "scene_COLLEGE_Coridor_8_base"
    return

label college_coridor8_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Student18", {"type" : 2, "base" : "COLLEGE_Coridor_8_Student18_[collegeStudent18_Suffix]", "click" : "college_coridor8_environment", "actions" : "l", "zorder":5, "selectable": False, "group":"students"}, scene="college_coridor8")

    $ add_object_to_scene("Teleport_Coridor9", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_8_Teleport_Coridor9", "click" : "college_coridor8_environment", "xpos" : 1344, "ypos" : 948, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor8")
    $ add_object_to_scene("Teleport_Principal_Secretary", {"type":3, "text" : t_("ПРИЕМНАЯ ДИРЕКТОРА"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_8_Teleport_Principal_Secretary", "click" : "college_coridor8_environment", "xpos" : 1111, "ypos" : 227, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor8")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor8_environment:
    if obj_name == "Teleport_Coridor9":
        call change_scene("college_coridor9") from _rcall_change_scene_55
        return
    if obj_name == "Teleport_Principal_Secretary":
        call change_scene("college_principal_secretary") from _rcall_change_scene_56
        return
    return
