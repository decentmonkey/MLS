label arnie_street:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "scene_PRINCIPAL_Street[day_suffix]"
    return

label arnie_street_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "arnie_street_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="arnie_street")
    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("ВХОД В ДОМ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "arnie_street_environment", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True, "group":"teleports"}, scene="arnie_street")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label arnie_street_environment:
    if obj_name == "Teleport_Map":
        call map_show() from _rcall_map_show_4
        return
    if obj_name == "Teleport_LivingRoom":
        call ep01_dialogues2_day1_family_1_12() from _rcall_ep01_dialogues2_day1_family_1_12
        return
    return
