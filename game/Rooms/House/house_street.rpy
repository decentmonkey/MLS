label house_street:
    $ miniMapData = []
    $ sceneIsStreet = True
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate_13
    $ scene_image = "scene_House_Street[day_suffix]"
    if day_time_idx <= 1:
        music rich_hotel_park
    else:
        music night_ambience
    return

label house_street_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "house_street_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True}, scene="house_street")
    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ВХОД В ДОМ"), "larrow" : "arrow_down_2_a", "base":"House_Street_Teleport_Floor1", "click" : "house_street_environment", "xpos" : 1391, "ypos" : 429, "zorder":11, "teleport":True}, scene="house_street")
    $ add_object_to_scene("Teleport_Garage", {"type":3, "text" : t_("ГАРАЖ"), "rarrow" : "arrow_down_2", "base":"House_Street_Teleport_Garage", "click" : "house_street_environment", "xpos" : 322, "ypos" : 417, "zorder":11, "teleport":True}, scene="house_street")
    $ add_object_to_scene("Teleport_StoreRoom", {"type":3, "text" : t_("ПОДВАЛ"), "larrow" : "arrow_down_2_a", "base":"empty", "click" : "house_street_environment", "xpos" : 1638, "ypos" : 520, "zorder":11, "teleport":True}, scene="house_street")
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
        call map_show() from _rcall_map_show_2
        return
    if obj_name == "Teleport_Floor1":
        call change_scene("house_floor1") from _rcall_change_scene_104
        return
    if obj_name == "Teleport_Garage":
        call change_scene("house_garage") from _rcall_change_scene_105
        return
    if obj_name == "Teleport_StoreRoom":
        call change_scene("house_storeroom") from _rcall_change_scene_106
        return

    return
