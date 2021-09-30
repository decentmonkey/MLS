default collegeStudent1_Suffix = 1
default collegeStudent2_Suffix = 1
default collegeStudent3_Suffix = 1

label college_coridor1:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate()
    $ scene_image = "scene_COLLEGE_Coridor_1_base"
    return

label college_coridor1_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Student1", {"type" : 2, "base" : "COLLEGE_Coridor_1_Student1_[collegeStudent1_Suffix]", "click" : "college_coridor1_environment", "actions" : "l", "zorder":3, "selectable": False, "group":"students"}, scene="college_coridor1")
    $ add_object_to_scene("Student2", {"type" : 2, "base" : "COLLEGE_Coridor_1_Student2_[collegeStudent2_Suffix]", "click" : "college_coridor1_environment", "actions" : "l", "zorder":1, "selectable": False, "group":"students"}, scene="college_coridor1")
    $ add_object_to_scene("Student3", {"type" : 2, "base" : "COLLEGE_Coridor_1_Student3_[collegeStudent3_Suffix]", "click" : "college_coridor1_environment", "actions" : "l", "zorder":10, "selectable": False, "group":"students"}, scene="college_coridor1")

    $ add_object_to_scene("Teleport_Biology", {"type":3, "text" : t_("БИОЛОГИЯ"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Coridor_1_Teleport_Biology", "click" : "college_coridor1_environment", "xpos" : 1053, "ypos" : 141, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor1")
    $ add_object_to_scene("Teleport_Hall", {"type":3, "text" : t_("АКТОВЫЙ ЗАЛ"), "larrow" : "arrow_down_2_a", "base":"COLLEGE_Coridor_1_Teleport_Hall", "click" : "college_coridor1_environment", "xpos" : 279, "ypos" : 178, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor1")
    $ add_object_to_scene("Teleport_LockerMC", {"type":3, "text" : t_("ШКАФЧИК"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_1_Teleport_LockerMC", "click" : "college_coridor1_environment", "xpos" : 1416, "ypos" : 266, "zorder":11, "teleport":True, "group":"teleports", "b":0.2, "tint":[1.0, 1.0, 0.8]}, scene="college_coridor1")
    $ add_object_to_scene("Teleport_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "larrow" : "arrow_down_2_a", "base":"COLLEGE_Coridor_1_Teleport_Stairs", "click" : "college_coridor1_environment", "xpos" : 743, "ypos" : 264, "zorder":0, "teleport":True, "group":"teleports"}, scene="college_coridor1")
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("УЛИЦА"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_coridor1_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports", "high_sprite_hover": True}, scene="college_coridor1")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor1_environment:
    if obj_name == "Teleport_Biology":
        call change_scene("college_biology")
        return
    if obj_name == "Teleport_Hall":
        call change_scene("college_hall")
        return
    if obj_name == "Teleport_LockerMC":
        call change_scene("college_lockermc")
        return
    if obj_name == "Teleport_Stairs":
        call change_scene("college_coridor3")
        return
    if obj_name == "Teleport_Street":
        call change_scene("college_street")
        return
    return
