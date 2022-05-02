default ep14_update_init_flag = False

label ep14_update_init:
    if ep14_update_init_flag == True:
        return
    $ ep14_update_init_flag = True
    $ remove_hook(quest="college_day3")
    $ remove_hook(quest="day4")
    call change_scene("house_bedroom_mc")
    call changeDayTime("morning")
    call ep04_dialogues1_family_sophie_1a()
    python:
        move_object("Sophie", "house_kitchen")
        move_object("Henry", "empty")
        move_object("Sister1", "house_sister1")
        move_object("Sister2", "house_sister2")
        sister1RoomDoorLocked = True
        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True
        sophieCallStage = 0
        map_enabled = False
        miniMapDisabled["HOUSE"] = ["House_Street"]

        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Floor1", scene="house_floor2")
        set_object_follow("Teleport_Bathroom", scene="house_floor1")
        set_object_follow("Teleport_Kitchen", scene="house_floor1")
        set_object_follow("Floor1", scene="minimap")

        questHelp("house_22")

        add_hook("before_open", "ep14_quests1_sophie", scene="house_kitchen", once=True, quest="day5")

    call refresh_scene_fade_long()
    return

label ep14_quests1_sophie:
    call ep04_dialogues1_family_sophie_1()
    return

