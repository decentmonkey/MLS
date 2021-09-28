label house_floor2:
    $ miniMapData = []
    $ scene_image = "scene_House_Floor2[day_suffix]"
    return

label house_floor2_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Sister2", {"type" : 2, "base" : "House_Floor2_Teleport_Sister2", "click" : "house_floor2_environment", "actions" : "l", "zorder":0, "teleport":True}, scene="house_floor2")
    $ add_object_to_scene("Teleport_Sister1", {"type" : 2, "base" : "House_Floor2_Teleport_Sister1", "click" : "house_floor2_environment", "actions" : "l", "zorder":0, "teleport":True}, scene="house_floor2")
    $ add_object_to_scene("Teleport_Bedroom_Landlord", {"type" : 2, "base" : "House_Floor2_Teleport_Bedroom_Landlord", "click" : "house_floor2_environment", "actions" : "l", "zorder":0, "teleport":True}, scene="house_floor2")

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ЛЕСТНИЦА ВНИЗ"), "rarrow" : "arrow_up_2", "base":"House_Floor2_Teleport_Floor1", "click" : "house_floor2_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_floor2")
    $ add_object_to_scene("Teleport_Bedroom_MC", {"type":3, "text" : t_("МОЯ КОМНАТА"), "larrow" : "arrow_up_2_a", "base":"House_Floor2_Teleport_Bedroom_MC", "click" : "house_floor2_environment", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_floor2")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_floor2_environment:
    if obj_name == "Teleport_Sister2":
        call change_scene("house_sister2")
        return
    if obj_name == "Teleport_Sister1":
        call change_scene("house_sister1")
        return
    if obj_name == "Teleport_Bedroom_Landlord":
        call change_scene("house_bedroom_landlord")
        return
    if obj_name == "Teleport_Floor1":
        call change_scene("house_floor1")
        return
    if obj_name == "Teleport_Bedroom_MC":
        call change_scene("house_bedroom_mc")
        return
    return
