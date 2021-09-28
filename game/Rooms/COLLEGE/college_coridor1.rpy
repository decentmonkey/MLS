label college_coridor1:
    $ miniMapData = []
    $ scene_image = "scene_COLLEGE_Coridor1_base"
    return

label college_coridor1_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "college_coridor1_environment", "actions" : "l", "zorder":10}, scene="college_coridor1")

    $ add_object_to_scene("Teleport_Biology", {"type":3, "text" : t_("БИОЛОГИЯ"), "larrow" : "arrow_down_2", "base":"COLLEGE_Coridor_1_Teleport_Biology", "click" : "college_coridor1_environment", "xpos" : 1053, "ypos" : 141, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor1")
    $ add_object_to_scene("Teleport_Hall", {"type":3, "text" : t_("АКТОВЫЙ ЗАЛ"), "rarrow" : "arrow_down_2", "base":"COLLEGE_Coridor_1_Teleport_Hall", "click" : "college_coridor1_environment", "xpos" : 279, "ypos" : 128, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor1")
    $ add_object_to_scene("Teleport_LockerMC", {"type":3, "text" : t_("ШКАФЧИК"), "rarrow" : "arrow_right_2", "base":"COLLEGE_Coridor_1_Teleport_LockerMC", "click" : "college_coridor1_environment", "xpos" : 1416, "ypos" : 266, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor1")
    $ add_object_to_scene("Teleport_Stairs", {"type":3, "text" : t_("ЛЕСТНИЦА"), "larrow" : "arrow_down_2", "base":"COLLEGE_Coridor_1_Teleport_Stairs", "click" : "college_coridor1_environment", "xpos" : 763, "ypos" : 244, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor1")
    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("УЛИЦА"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "college_coridor1_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="college_coridor1")
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
    if obj_name == "Teleport_LockerMC":
        call change_scene("college_lockermc")
    if obj_name == "Teleport_Stairs":
        call change_scene("college_coridor3")
    if obj_name == "Teleport_Hall":
        call change_scene("college_street")
        return
    return
