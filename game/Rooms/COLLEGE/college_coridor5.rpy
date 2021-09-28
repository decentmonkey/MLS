default collegeStudent11_Suffix = 1
default collegeStudent12_Suffix = 1

label college_coridor5:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate()
    $ scene_image = "scene_COLLEGE_Coridor_5_base"
    return

label college_coridor5_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Student11", {"type" : 2, "base" : "COLLEGE_Coridor_5_Student11_[collegeStudent11_Suffix]", "click" : "college_coridor5_environment", "actions" : "l", "zorder":10, "selectable": False, "group":"students"}, scene="college_coridor5")
    $ add_object_to_scene("Student12", {"type" : 2, "base" : "COLLEGE_Coridor_5_Student12_[collegeStudent12_Suffix]", "click" : "college_coridor5_environment", "actions" : "l", "zorder":10, "selectable": False, "group":"students"}, scene="college_coridor5")

    $ add_object_to_scene("Teleport_Coridor6", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_5_Teleport_Coridor6", "click" : "college_coridor5_environment", "xpos" : 1450, "ypos" : 903, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor5")
    $ add_object_to_scene("Teleport_Algebra", {"type":3, "text" : t_("АЛГЕБРА"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Coridor_5_Teleport_Algebra", "click" : "college_coridor5_environment", "xpos" : 1415, "ypos" : 189, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor5")
    $ add_object_to_scene("Teleport_ArtClass", {"type":3, "text" : t_("КЛАСС РИСОВАНИЯ"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_5_Teleport_ArtClass", "click" : "college_coridor5_environment", "xpos" : 574, "ypos" : 972, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor5")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor5_environment:
    if obj_name == "Teleport_Coridor6":
        call change_scene("college_coridor6")
        return
    if obj_name == "Teleport_Algebra":
        call change_scene("college_algebra")
        return
    if obj_name == "Teleport_ArtClass":
        call change_scene("college_artclass")
        return
    return
