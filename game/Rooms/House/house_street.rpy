label %scene%:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "[day_suffix]"
    return

label %scene%_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "%scene%_environment", "actions" : "l", "zorder":10}, scene="%scene%")

    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "%scene%_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="%scene%")
    $ add_object_to_scene("Teleport_Bedroom2", {"type":3, "text" : t_("ГАРДЕРОБ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "%scene%_environment", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True, "group":"teleports"}, scene="%scene%")
    $ add_object_to_scene("Teleport_Bedroom1", {"type":3, "text" : t_("КРОВАТЬ"), "larrow" : "arrow_left_2", "base":"Screen_Left_Arrow_Tight", "click" : "%scene%_environment", "xpos" : 220, "ypos" : 545, "zorder":11, "teleport":True, "group":"teleports"}, scene="%scene%")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label %scene%_environment:
    if obj_name == "Teleport_Map":
        call map_show()
        return
    if obj_name == "Teleport_Floor1":
        call change_scene("house_street_floor1")
        return
    return
label house_street:
    $ miniMapData = []
    $ sceneIsStreet = True
    call miniMapHouseGenerate()
    $ scene_image = "scene_House_Street[day_suffix]"
    music night_ambience
    return

label house_street_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "house_street_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="house_street")
    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ВХОД В ДОМ"), "larrow" : "arrow_down_2", "base":"House_Street_Teleport_Floor1", "click" : "house_street_environment", "xpos" : 1391, "ypos" : 429, "zorder":11, "teleport":True}, scene="house_street")
    $ add_object_to_scene("Teleport_Garage", {"type":3, "text" : t_("ГАРАЖ"), "rarrow" : "arrow_down_2", "base":"House_Street_Teleport_Garage", "click" : "house_street_environment", "xpos" : 322, "ypos" : 417, "zorder":11, "teleport":True}, scene="house_street")
    $ add_object_to_scene("Teleport_StoreRoom", {"type":3, "text" : t_("ПОДВАЛ"), "larrow" : "arrow_down_2", "base":"empty", "click" : "house_street_environment", "xpos" : 1638, "ypos" : 520, "zorder":11, "teleport":True}, scene="house_street")
    return


#	House_Street_Teleport_Floor1 - ВХОД В ДОМ 1391x429 left arrow_down_2, teleport House_Floor1
#	House_Street_Teleport_Garage - ГАРАЖ 322x417 right arrow_down_2, teleport House_Garage
#	House_Street_Teleport_StoreRoom - ПОДВАЛ 1638x520 left arrow_down_2, teleport House_StoreRoom
#	House_Street_Teleport_Map - ГОРОД (Screen_Down_Arrow), open map


#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_street_environment:
    if obj_name == "Teleport_Map":
        call map_show()
        return
    if obj_name == "Teleport_Floor1":
        call change_scene("house_street_floor1")
        return
    if obj_name == "Teleport_Garage":
        call change_scene("house_street_garage")
        return
    if obj_name == "Teleport_StoreRoom":
        call change_scene("house_street_storeroom")
        return

    return
