label housefriend_kitchen:
    $ miniMapData = []
    $ scene_image = "scene_HouseFriend_Kitchen[day_suffix]"
    return

label housefriend_kitchen_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "housefriend_kitchen_environment", "actions" : "l", "zorder":10}, scene="housefriend_kitchen")

    $ add_object_to_scene("Teleport_LivingRoom", {"type":3, "text" : t_("НАЗАД В ГОСТИНУЮ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "housefriend_kitchen_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_kitchen")
    $ add_object_to_scene("Teleport_Bedroom_Parents", {"type":3, "text" : t_("СПАЛЬНЯ РОДИТЕЛЕЙ ШОНА"), "larrow" : "arrow_left_2", "base":"HouseFriend_Kitchen_Teleport_Bedroom_Parents", "click" : "housefriend_kitchen_environment", "xpos" : 642, "ypos" : 218, "zorder":11, "teleport":True, "group":"teleports"}, scene="housefriend_kitchen")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label housefriend_kitchen_environment:
    if obj_name == "Teleport_LivingRoom":
        call change_scene("housefriend_livingroom")
        return
    if obj_name == "Teleport_Bedroom_Parents":
        call change_scene("housefriend_bedroom_parents")
        return
    return
