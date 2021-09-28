default collegeStreetCrowd1_Suffix = 1
default collegeStreetCrowd1_Suffix = 2
default collegeStreetCrowd1_Suffix = 3
default collegeStreetCrowd1_Suffix = 4
default collegeStreetCrowd1_Suffix = 5
default collegeStreetCrowd1_Suffix = 6
default collegeStreetCrowd1_Suffix = 7
default collegeStreetCrowd1_Suffix = 8
default collegeStreetCrowd1_Suffix = 9
default collegeStreetCrowd1_Suffix = 10
default collegeStreetFriendBardie_Suffix = 1
default collegeStreetClassmate1_Suffix = 1

label college_street:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate()
    $ sceneIsStreet = True
    if day_time_idx == 3:
        $ scene_image = "scene_COLLEGE_Street_Night"
    else:
        $ scene_image = "scene_COLLEGE_Street[day_suffix]"
    return

label college_street_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Crowd1", {"type" : 2, "base" : "COLLEGE_Street_Crowd1_[collegeStreetCrowd1_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Crowd2", {"type" : 2, "base" : "COLLEGE_Street_Crowd2_[collegeStreetCrowd2_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Crowd3", {"type" : 2, "base" : "COLLEGE_Street_Crowd3_[collegeStreetCrowd3_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Crowd4", {"type" : 2, "base" : "COLLEGE_Street_Crowd4_[collegeStreetCrowd4_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Crowd5", {"type" : 2, "base" : "COLLEGE_Street_Crowd5_[collegeStreetCrowd5_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Crowd6", {"type" : 2, "base" : "COLLEGE_Street_Crowd6_[collegeStreetCrowd6_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Crowd7", {"type" : 2, "base" : "COLLEGE_Street_Crowd7_[collegeStreetCrowd7_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Crowd8", {"type" : 2, "base" : "COLLEGE_Street_Crowd8_[collegeStreetCrowd8_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Crowd9", {"type" : 2, "base" : "COLLEGE_Street_Crowd9_[collegeStreetCrowd9_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Crowd10", {"type" : 2, "base" : "COLLEGE_Street_Crowd10_[collegeStreetCrowd10_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Classmate1", {"type" : 2, "base" : "COLLEGE_Street_Classmate1_[collegeStreetClassmate1_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10, "selectable": False}, scene="college_street")
    $ add_object_to_scene("Friend_Bardie", {"type" : 2, "base" : "COLLEGE_Street_Friend_Bardie_[collegeStreetFriendBardie_Suffix][day_suffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10}, scene="college_street")

    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_street_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_street")
    $ add_object_to_scene("Teleport_Coridor1", {"type":3, "text" : t_("ВХОД В КОЛЛЕДЖ"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Street_Teleport_Coridor1", "click" : "college_street_environment", "xpos" : 1138, "ypos" : 555, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_street")
    $ add_object_to_scene("Teleport_StreetYard", {"type":3, "text" : t_("СПОРТИВНАЯ ПЛОЩАДКА"), "larrow" : "arrow_down_2_a", "base":"COLLEGE_Street_Teleport_StreetYard", "click" : "college_street_environment", "xpos" : 498, "ypos" : 537, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_street")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_street_environment:
    if obj_name == "Teleport_Map":
        call map_show()
        return
    if obj_name == "Teleport_Coridor1":
        call change_scene("college_coridor1")
        return
    if obj_name == "Teleport_StreetYard":
        call change_scene("college_streetyard")
        return
    return
