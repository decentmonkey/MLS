label college_coridor3:
    $ miniMapData = []
    call miniMapCOLLEGEGenerate()
    $ scene_image = "scene_COLLEGE_Coridor_3_base"
    return

label college_coridor3_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "college_coridor3_environment", "actions" : "l", "zorder":10}, scene="college_coridor3")

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ЭТАЖ 2"), "larrow" : "arrow_left_2", "base":"COLLEGE_Coridor_3_Teleport_Floor2", "click" : "college_coridor3_environment", "xpos" : 561, "ypos" : 81, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor3")
    $ add_object_to_scene("Teleport_Coridor2", {"type":3, "text" : t_("КОРИДОР"), "rarrow" : "arrow_up_2", "base":"COLLEGE_Coridor_3_Teleport_Coridor2", "click" : "college_coridor3_environment", "xpos" : 1644, "ypos" : 806, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor3")
    $ add_object_to_scene("Teleport_Geography", {"type":3, "text" : t_("ГЕОГРАФИЯ"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_3_Teleport_Geography", "click" : "college_coridor3_environment", "xpos" : 1120, "ypos" : 180, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor3")

    $ add_object_to_scene("Teleport_Coridor1", {"type":3, "text" : t_("ВХОД В КОЛЛЕДЖ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_coridor3_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor3")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label college_coridor3_environment:
    if obj_name == "Teleport_Coridor1":
        call change_scene("college_coridor1")
        return
    if obj_name == "Teleport_Floor2":
        call college_stairs_menu()
        return
    if obj_name == "Teleport_Coridor2":
        call change_scene("college_coridor2")
        return
    if obj_name == "Teleport_Geography":
        call change_scene("college_geography")
        return
    return
