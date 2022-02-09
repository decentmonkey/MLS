label ep13_quests_init:
    call changeDayTime("morning")
    call ep03_dialogues1_family_morning_1()
    python:
        remove_hook(label="ep12_quests20_home")
        remove_hook(quest="day2")

        map_enabled = False
        add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block", quest="day3")
        miniMapDisabled["HOUSE"] = ["House_Street"]
        sister1RoomDoorLocked = True
        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True
        sophieCallStage = 0
        questHelp("house_16", True)
        questHelp("house_17")
        questHelp("house_18")
        move_object("Sophie", "house_kitchen")
        move_object("Henry", "empty")
        move_object("Sister1", "house_sister1")
        move_object("Sister2", "house_sister2")

        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Floor1", scene="house_floor2")
        set_object_follow("Teleport_Bathroom", scene="house_floor1")
        set_object_follow("Teleport_Kitchen", scene="house_floor1")
        set_object_follow("Floor1", scene="minimap")


        add_hook("Shower", "ep13_quests2_bathroom", scene="house_bathroom", quest="day3")
        add_hook("before_open", "ep13_quests2_bathroom", scene="house_bathroom", quest="day3")
        add_hook("before_open", "ep13_quests2_kitchen", scene="house_kitchen", once=True, quest="day3")

    call refresh_scene_fade_long()
    return

label ep13_quests2_bathroom:
    call ep03_dialogues1_family_morning_1a()
    if _return == False:
        call refresh_scene_fade()
        return False
    $ remove_hook(label="ep13_quests2_bathroom")
    $ questHelp("house_18", True)
    return False

label ep13_quests2_kitchen:
    call ep03_dialogues1_family_morning_2()
    $ map_enabled = True
    $ miniMapDisabled["HOUSE"] = []
    $ questHelp("house_17", True)
    $ questHelp("college_25")
    $ clear_object_follow_all()
    $ remove_hook(label="house_block")
    $ add_hook("Teleport_Coridor1", "ep13_quests3_college_enter", scene="college_street", quest="day3", once=True)
    $ set_object_follow("Teleport_Floor1", scene="house_kitchen")
    $ set_object_follow("Teleport_Street", scene="house_floor1")
    $ set_object_follow("House_Street", scene="minimap")
    $ set_object_follow("Teleport_COLLEGE", scene="map")
    $ set_object_follow("Teleport_Coridor1", scene="college_street")
    return

label ep13_quests3_college_enter:
    $ cynthiaCallStage = 2
    $ questHelp("college_25", True)
    if questHelpGetStatus("house_18") == 0: # если не принимали душ, то fail
        $ questHelp("house_18", False)
        $ remove_hook(label="ep13_quests2_bathroom")
    
    call ep03_dialogues2_college_1()
    call ep03_dialogues2_college_2()
    $ miniMapEnabledOnly = ["none"]
    $ set_object_follow("Teleport_English", scene="college_coridor6")

    $ clear_object_follow_all()


    # блокировка перемещений
    $ add_hook("Teleport_Coridor7", "ep03_dialogues2_college_2a", scene="college_coridor6", quest="college_day3", label="english_lesson")
    $ add_hook("Teleport_Coridor5", "ep03_dialogues2_college_2a", scene="college_coridor6", quest="college_day3", label="english_lesson")
    $ add_hook("Teleport_English", "ep13_quests3_english_lesson", scene="college_coridor6", quest="college_day3", label="english_lesson")

#    $ set_active("Student14", False, scene="college_coridor6")

    $ questHelp("college_26")
    call change_scene("college_coridor6", "Fade_long")
    return False

label ep13_quests3_english_lesson:
    call change_scene("college_english")
    $ questHelp("college_26", True)
    $ remove_hook(label="english_lesson")
    $ miniMapEnabledOnly = []
    call ep03_dialogues2_college_3()
    # пишем Шону
    $ seanCallStage = 4
    call phone_outgoing_call("Sean", "sean_chat5")
    call ep03_dialogues2_college_3next1()

    $ miniMapDisabled["COLLEGE"] = []

    $ add_hook("enter_scene", "ep13_quests3_english_after", scene="college_coridor6", once=True)

    call change_scene("college_coridor6", "Fade_long")
    return False

label ep13_quests3_english_after:
    call ep03_dialogues2_college_3a()
    $ sophieCallStage = 3
    # sophie_chat4
    $ phone_incoming_call("Sophie")
    $ add_hook("phone_close", "ep13_quests3_english_after2", scene="phone", once=True, quest="college_day3")
    return

label ep13_quests3_english_after2:
    python:
        seanCallStage = 0
        set_active("Teleport_ArtClass", True, scene="college_coridor5")
        remove_hook(quest="college_day2")
        sophieCallStage = 0
        questHelp("work_1")
        add_hook("Teleport_English", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="college_coridor6", quest="college_day3")
        rooms_list = get_rooms_recursive("COLLEGE")
    return
        for room_name1 in rooms_list:
            add_hook("before_open", "ep13_quests4_maurice_meet", scene=room_name1, label="maurice_meet")
    return

label ep13_quests4_maurice_meet:
    $ remove_hook(label="maurice_meet")
    call ep03_dialogues2_college_4()
    call ep03_dialogues2_college_5()

    python:
        add_hook("Teleport_ArtClass", "ep03_dialogues2_college_9", scene="college_coridor5", quest="college_day3")
        add_hook("Teleport_Principal_Secretary", "ep03_dialogues2_college_9", scene="college_coridor8", quest="college_day3")

        add_hook("Teleport_Library", "ep13_quests5_college_walk", scene="college_coridor9", quest="college_day3")
        add_hook("Teleport_Gym", "ep13_quests5_college_walk", scene="college_coridor2", quest="college_day3")
        add_hook("Teleport_Algebra", "ep13_quests5_college_walk", scene="college_coridor5", quest="college_day3")

        add_hook("before_open", "ep13_quests5_college_end", scene="college_street", quest="college_day3", once=True)
    return

label ep13_quests5_college_walk:
    if obj_name == "Teleport_Library":
        call ep03_dialogues2_college_6()
    if obj_name == "Teleport_Gym":
        call ep03_dialogues2_college_7()
    if obj_name == "Teleport_Algebra":
        call ep03_dialogues2_college_8()
    call refresh_scene_fade()
    return False

label ep13_quests5_college_end:
    call ep03_dialogues2_college_5a()
    call ep03_dialogues2_college_10()
    $ remove_hook(label="college_day3")
    return



