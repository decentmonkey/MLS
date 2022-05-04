default mallStreetWhoreSuffix = 1

label mall_street:
    $ miniMapData = []
    $ sceneIsStreet = True
    $ scene_image = "scene_MALL_Street[day_suffix]"
    return

label mall_street_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("ВХОД В ДОМ"), "larrow" : "arrow_down_2_a", "base":"AUNTIE_Street_Enter", "click" : "mall_street_environment", "xpos" : 1280, "ypos" : 520, "zorder":11, "teleport":True, "group":"teleports", "b":0.2, "tint":[1.0, 1.0, 0.8]}, scene="mall_street")
    $ add_object_to_scene("Whore", {"type" : 2, "base" : "MALL_Street_Whore[mallStreetWhoreSuffix][day_suffix]", "click" : "mall_street_environment", "actions" : "l", "zorder":10}, scene="mall_street")

    $ add_object_to_scene("Teleport_Map", {"type":3, "text" : t_("ГОРОД"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "mall_street_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="mall_street")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label mall_street_environment:
    if obj_name == "Teleport_Map":
        call map_show()
        return
#        call change_scene("daisy_livingroom")
#        return
    return
