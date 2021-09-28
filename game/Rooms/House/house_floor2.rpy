label house_floor2:
    $ miniMapData = []
    call miniMapHouseGenerate()
    $ scene_image = "scene_House_Floor2[day_suffix]"
    if day_time_idx == 3:
        $ scene_image = "scene_House_Floor2_Evening_Night"
    return

label house_floor2_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Teleport_Sister2", {"type" : 2, "base" : "House_Floor2_Teleport_Sister2", "click" : "house_floor2_environment", "actions" : "l", "zorder":0, "teleport":True}, scene="house_floor2")
    $ add_object_to_scene("Teleport_Sister1", {"type" : 2, "base" : "House_Floor2_Teleport_Sister1", "click" : "house_floor2_environment", "actions" : "l", "zorder":0, "teleport":True}, scene="house_floor2")
    $ add_object_to_scene("Teleport_Bedroom_Landlord", {"type" : 2, "base" : "House_Floor2_Teleport_Bedroom_Landlord", "click" : "house_floor2_environment", "actions" : "l", "zorder":0, "teleport":True}, scene="house_floor2")

    $ add_object_to_scene("FlipChart", {"type" : 2, "base" : "House_Floor2_FlipChart", "click" : "house_floor2_environment", "actions" : "l", "zorder":0}, scene="house_floor2")
    $ add_object_to_scene("Picture1", {"type" : 2, "base" : "House_Floor2_Picture1", "click" : "house_floor2_environment", "actions" : "l", "zorder":0}, scene="house_floor2")
    $ add_object_to_scene("Picture2", {"type" : 2, "base" : "House_Floor2_Picture2", "click" : "house_floor2_environment", "actions" : "l", "zorder":0}, scene="house_floor2")

    $ add_object_to_scene("Teleport_Floor1", {"type":3, "text" : t_("ЛЕСТНИЦА ВНИЗ"), "rarrow" : "arrow_up_2", "base":"House_Floor2_Teleport_Floor1", "click" : "house_floor2_environment", "xpos" : 1342, "ypos" : 1013, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_floor2")
    $ add_object_to_scene("Teleport_Bedroom_MC", {"type":3, "text" : t_("МОЯ КОМНАТА"), "larrow" : "arrow_up_2_a", "base":"House_Floor2_Teleport_Bedroom_MC", "click" : "house_floor2_environment", "xpos" : 362, "ypos" : 957, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_floor2")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_floor2_environment:
    if obj_name == "FlipChart":
        call ep01_dialogues2_day1_family_1_7()
        $ open_secret_object(obj_name)
        return
    if obj_name == "Picture1" or obj_name == "Picture2":
        call ep01_dialogues2_day1_family_1_9()
        return
    if obj_name == "Teleport_Sister2":
        if sister2RoomDoorLocked == True:
            sound snd_door_locked1
            pause 1.0
            call ep01_dialogues2_day1_family_1_6()
            return
        call change_scene("house_sister2", "Fade", "snd_door_open1")
        return
    if obj_name == "Teleport_Sister1":
        if sister1RoomDoorLocked == True:
            sound snd_door_locked1
            pause 1.0
            call ep01_dialogues2_day1_family_1_6()
            return
        call change_scene("house_sister1", "Fade", "snd_door_open1")
        return
    if obj_name == "Teleport_Bedroom_Landlord":
        if landLordRoomDoorLocked == True:
            sound snd_door_locked1
            pause 1.0
            call ep01_dialogues2_day1_family_1_6()
            return
        call change_scene("house_bedroom_landlord", "Fade", "snd_door_open1")
        return
    if obj_name == "Teleport_Floor1":
        call change_scene("house_floor1")
        return
    if obj_name == "Teleport_Bedroom_MC":
        call change_scene("house_bedroom_mc")
        return
    return
