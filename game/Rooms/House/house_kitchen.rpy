label house_kitchen:
    $ miniMapData = []
    $ scene_image = "scene_House_Kitchen[day_suffix]"
    return

label house_kitchen_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "house_kitchen_environment", "actions" : "l", "zorder":10}, scene="house_kitchen")

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("НАЗАД"), "rarrow" : "arrow_right_2", "base":"House_Kitchen_Teleport_Floor1", "click" : "house_kitchen_environment", "xpos" : 1604, "ypos" : 573, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_kitchen")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_kitchen_environment:
    if obj_name == "Teleport_Floor1":
        call change_scene("house_floor1")
        return
    return
