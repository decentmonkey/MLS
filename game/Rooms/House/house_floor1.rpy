label house_floor1:
    $ miniMapData = []
    call miniMapHouseGenerate()
    $ scene_image = "scene_House_Floor1[day_suffix]"
    return

label house_floor1_init:
    $ default_tint = [1.0, 1.0, 1.0]
#    $ add_object_to_scene("Monica", {"type" : 2, "base" : "basement_bedroom1_Monica_[basementBedroom1MonicaSuffix]", "click" : "house_floor1_environment", "actions" : "l", "zorder":10}, scene="house_floor1")

    $ add_object_to_scene("Teleport_LivingRoomHall", {"type" : 2, "base" : "House_Floor1_Teleport_LivingRoomHall", "click" : "house_floor1_environment", "actions" : "l", "zorder":0, "teleport":True}, scene="house_floor1")
    $ add_object_to_scene("Teleport_Kitchen", {"type" : 2, "base" : "House_Floor1_Teleport_Kitchen", "click" : "house_floor1_environment", "actions" : "l", "zorder":0, "teleport":True}, scene="house_floor1")
    $ add_object_to_scene("Teleport_Bathroom", {"type" : 2, "base" : "House_Floor1_Teleport_Bathroom", "click" : "house_floor1_environment", "actions" : "l", "zorder":0, "teleport":True}, scene="house_floor1")

    $ add_object_to_scene("Teleport_Street", {"type":3, "text" : t_("УЛИЦА"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "house_floor1_environment", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_floor1")
    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ВТОРОЙ ЭТАЖ"), "larrow" : "arrow_up_2_a", "base":"House_Floor1_Teleport_Floor2", "click" : "house_floor1_environment", "xpos" : 450, "ypos" : 946, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_floor1")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_floor1_environment:
    if obj_name == "Teleport_LivingRoomHall":
        call change_scene("house_livingroomhall")
        return
    if obj_name == "Teleport_Kitchen":
        call change_scene("house_kitchen")
        return
    if obj_name == "Teleport_Bathroom":
        call change_scene("house_bathroom")
        return
    if obj_name == "Teleport_Street":
        call change_scene("house_street")
        return
    if obj_name == "Teleport_Floor2":
        call change_scene("house_floor2")
        return
    return
