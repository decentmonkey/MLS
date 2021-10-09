default collegeStudent13_Suffix = 1
default collegeStudent14_Suffix = 1
default collegeStudent20_Suffix = 1

label college_coridor6:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_6
    $ scene_image = "scene_COLLEGE_Coridor_6_base"
    return

label college_coridor6_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Student13", {"type" : 2, "base" : "COLLEGE_Coridor_6_Student13_[collegeStudent13_Suffix]", "click" : "college_coridor6_environment", "actions" : "l", "zorder":5, "selectable": False, "group":"students"}, scene="college_coridor6")
    $ add_object_to_scene("Student14", {"type" : 2, "base" : "COLLEGE_Coridor_6_Student14_[collegeStudent14_Suffix]", "click" : "college_coridor6_environment", "actions" : "l", "zorder":8, "selectable": False, "group":"students"}, scene="college_coridor6")
    $ add_object_to_scene("Student20", {"type" : 2, "base" : "COLLEGE_Coridor_6_Student20_[collegeStudent20_Suffix]", "click" : "college_coridor6_environment", "actions" : "l", "zorder":10, "selectable": False, "group":"students"}, scene="college_coridor6")

    $ add_object_to_scene("Teleport_Coridor7", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_6_Teleport_Coridor7", "click" : "college_coridor6_environment", "xpos" : 1393, "ypos" : 951, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor6")
    $ add_object_to_scene("Teleport_English", {"type":3, "text" : t_("АНГЛИЙСКИЙ"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_6_Teleport_English", "click" : "college_coridor6_environment", "xpos" : 1747, "ypos" : 542, "zorder":1, "teleport":True, "group":"teleports"}, scene="college_coridor6")
    $ add_object_to_scene("Teleport_Physics", {"type":3, "text" : t_("ФИЗИКА"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_6_Teleport_Physics", "click" : "college_coridor6_environment", "xpos" : 1200, "ypos" : 238, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor6")
    $ add_object_to_scene("Teleport_Coridor5", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "college_coridor6_environment", "xpos" : 354, "ypos" : 471, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor6")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor6_environment:
    if obj_name == "Teleport_Coridor7":
        call change_scene("college_coridor7") from _rcall_change_scene_49
        return
    if obj_name == "Teleport_English":
        call change_scene("college_english") from _rcall_change_scene_50
        return
    if obj_name == "Teleport_Physics":
        call change_scene("college_physics") from _rcall_change_scene_51
        return
    if obj_name == "Teleport_Coridor5":
        call change_scene("college_coridor5") from _rcall_change_scene_52
        return
    return
