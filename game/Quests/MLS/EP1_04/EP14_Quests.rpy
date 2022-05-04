default ep14_update_init_flag = False

default sophieKitchenHelpEnabled1 = False
default sophieKitchenHelpLastDay = 0

label ep14_update_init:
    if ep14_update_init_flag == True:
        return
    $ day = day + 1
    $ ep14_update_init_flag = True
    $ remove_hook(quest="college_day3")
    $ remove_hook(quest="day4")
    call change_scene("house_bedroom_mc")
    call process_change_map_location("HOUSE")
    call changeDayTime("morning")
    call ep04_dialogues1_family_sophie_1a()
    python:
        sophieKitchenHelpEnabled1 = True

        move_object("Sophie", "house_kitchen")
        move_object("Henry", "empty")
        move_object("Sister1", "house_sister1")
        move_object("Sister2", "college_empty")
        move_object("Friend_Bardie", "college_empty")
        
        #move_object("Sister2", "house_sister2")
        sister1RoomDoorLocked = True
        #sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True
        sophieCallStage = 0
        seanCallStage = 0
        map_enabled = False
        miniMapDisabled["HOUSE"] = ["House_Street"]

        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Floor1", scene="house_floor2")
        set_object_follow("Teleport_Kitchen", scene="house_floor1")
        set_object_follow("Floor1", scene="minimap")

        questHelp("house_22")
        questHelp("house_23")

        add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block", quest="day5")
        add_hook("before_open", "ep14_quests1_sophie", scene="house_kitchen", once=True, quest="day5")

    call refresh_scene_fade_long()
    return

label ep14_quests1_sophie:
    call ep04_dialogues1_family_sophie_1()
    $ clear_object_follow_all()
    $ questHelp("house_22", True)
    $ questHelp("college_29")
    $ map_enabled = True
    $ miniMapDisabled["HOUSE"] = []
    $ set_object_follow("Floor1", scene="minimap")
    $ set_object_follow("Teleport_Floor1", scene="house_kitchen")
    $ set_object_follow("Teleport_Street", scene="house_floor1")
    $ set_object_follow("Teleport_Map", scene="house_street")
    $ set_object_follow("Teleport_COLLEGE", scene="map")
    $ set_object_follow("Teleport_Coridor1", scene="college_street")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor2", "COLLEGE_Floor3"]

    $ remove_hook(label="house_block")
    $ add_hook("Teleport_Coridor1", "ep14_quests2_college", scene="college_street", quest="day5", once=True)
    $ add_hook("before_open", "ep14_quests2_college", scene="college_coridor3", quest="day5", once=True)

    call refresh_scene_fade()
    return

label ep14_quests2_college:
    $ remove_hook(label="ep14_quests2_college")
    $ clear_object_follow_all()
    $ questHelp("college_29", True)
    call ep04_dialogues6_college_sarah_1()
    $ clear_object_follow_all()
    $ set_object_follow("Teleport_Gym", scene="college_coridor2")
    $ miniMapEnabledOnly = ["none"]
    $ set_active("Teleport_Stairs", False, scene="college_coridor2")
    $ add_hook("before_open", "ep14_quests2_college2_gym", scene="college_gym", quest="day5")


    call change_scene("college_coridor2", "Fade_long")


    return False

label ep14_quests2_college2_gym:
    $ clear_object_follow_all()
    call ep04_dialogues6_college_sarah_2()
    $ set_active("Teleport_Stairs", True, scene="college_coridor2")
    $ set_object_follow("Teleport_Coridor2", scene="college_gym")
    $ set_active("Teleport_Coridor2", True, scene="college_gym")
    $ miniMapEnabledOnly = []
    $ add_hook("Teleport_Coridor2", "ep14_quests2_college3_end", scene="college_gym", once=True)

    return False


label ep14_quests2_college3_end:
    $ clear_object_follow_all()
    call ep03_dialogues2_college_10b()
    call changeDayTime("day")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor1", "COLLEGE_Floor2", "COLLEGE_Floor3"]
#    $ autorun_to_object("", scene="college_street") # диалог что надо идти работать
    $ questHelp("work_4")
    $ questHelp("work_5")
    $ set_object_follow("Teleport_Map", scene="house_street")
    $ set_object_follow("Teleport_DAISY", scene="map")
    $ set_object_follow("Teleport_PARK", scene="map")
    $ add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", quest="day5")
    $ add_hook("Teleport_LivingRoom", "ep14_quests3_daisy1", scene="daisy_street", quest="daisy_work")
    call change_scene("college_street")
    return False

label ep14_quests3_daisy1:
    if day_time_idx > 1:
        return
    if mlsBardiFamilyV4Daisy2 > 0:
        call ep04_dialogues4_family_daisy_3()
    else:
        call ep04_dialogues4_family_daisy_1()
        call ep04_dialogues4_family_daisy_2()
        $ questHelp("work_4", True)
    return False

