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
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "college_street_environment", "actions" : "l", "zorder":10}, scene="college_street")

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
