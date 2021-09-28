label housefriend_street:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "scene_HouseFriend_Street[day_suffix]"
    return

label housefriend_street_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "housefriend_street_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_street")
    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("ВХОД В ДОМ"), "rarrow" : "arrow_right_2", "base":"HouseFriend_Street_Teleport_LivingRoom", "click" : "housefriend_street_environment", "xpos" : 753, "ypos" : 414, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_street")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label housefriend_street_environment:
    if obj_name == "Teleport_Map":
        call map_show()
        return
    if obj_name == "Teleport_LivingRoom":
        call change_scene("housefriend_livingroom")
        return
    return
