default collegeStudent15_Suffix = 1
default collegeStudent16_Suffix = 1
default collegeStudent17_Suffix = 1

label college_coridor7:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate() from _rcall_miniMapCOLLEGEGenerate_7
    $ scene_image = "scene_COLLEGE_Coridor_7_base"
    return

label college_coridor7_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Student15", {"type" : 2, "base" : "COLLEGE_Coridor_7_Student15_[collegeStudent15_Suffix]", "click" : "college_coridor7_environment", "actions" : "l", "zorder":1, "selectable": False, "group":"students"}, scene="college_coridor7")
    $ add_object_to_scene("Student16", {"type" : 2, "base" : "COLLEGE_Coridor_7_Student16_[collegeStudent16_Suffix]", "click" : "college_coridor7_environment", "actions" : "l", "zorder":10, "selectable": False, "group":"students"}, scene="college_coridor7")
    $ add_object_to_scene("Student17", {"type" : 2, "base" : "COLLEGE_Coridor_7_Student17_[collegeStudent17_Suffix]", "click" : "college_coridor7_environment", "actions" : "l", "zorder":10, "selectable": False, "group":"students"}, scene="college_coridor7")

    $ add_object_to_scene("Teleport_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_7_Teleport_Stairs", "click" : "college_coridor7_environment", "xpos" : 1416, "ypos" : 193, "zorder":0, "teleport":True, "group":"teleports"}, scene="college_coridor7")
    $ add_object_to_scene("Teleport_Computer", {"type":3, "text" : t_("КОМПЬЮТЕРНЫЙ КЛАСС"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Coridor_7_Teleport_Computer", "click" : "college_coridor7_environment", "xpos" : 525, "ypos" : 135, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor7")
    $ add_object_to_scene("Teleport_Coridor6", {"type":3, "text" : t_("КОРИДОР"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_7_Teleport_Coridor6", "click" : "college_coridor7_environment", "xpos" : 421, "ypos" : 945, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor7")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor7_environment:
    if obj_name == "Teleport_Stairs":
        call college_stairs_menu() from _rcall_college_stairs_menu_2
        return
    if obj_name == "Teleport_Computer":
        call change_scene("college_computer") from _rcall_change_scene_53
        return
    if obj_name == "Teleport_Coridor6":
        call change_scene("college_coridor6") from _rcall_change_scene_54
        return
    return
