label house_bedroom_landlord:
    $ miniMapData = []
    $ scene_image = "scene_House_Bedroom_Landlord[day_suffix]"
    return

label house_bedroom_landlord_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "house_bedroom_landlord_environment", "actions" : "l", "zorder":10}, scene="house_bedroom_landlord")

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_left_2", "base":"House_Bedroom_Landlord_Teleport_Floor2", "click" : "house_bedroom_landlord_environment", "xpos" : 334, "ypos" : 972, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_bedroom_landlord")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_bedroom_landlord_environment:
    if obj_name == "Teleport_Floor2":
        call change_scene("house_floor2")
        return
    return
