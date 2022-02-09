default ep13_update_init_flag = False
label ep13_update_init:
    if ep13_update_init_flag == True:
        return
    $ ep13_update_init_flag = True

    # +1 день
    $ day += 1
    $ week_day = (day)%7
    if week_day == 0:
        $ week_day = 7
    return

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
    $ set_object_follow("Teleport_Map", scene="house_street")
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
    $ clear_object_follow_all()
    $ set_object_follow("Teleport_English", scene="college_coridor6")



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
    call changeDayTime("day")
    $ set_active("Student14", False, scene="college_coridor6")

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
    call ep03_dialogues1_family_morning_4()
    python:
        seanCallStage = 0
        set_active("Teleport_ArtClass", True, scene="college_coridor5")
        remove_hook(quest="college_day2")
        sophieCallStage = 0
        questHelp("work_1")
        add_hook("Teleport_English", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="college_coridor6", quest="college_day3")
        rooms_list = get_rooms_recursive("COLLEGE")
        for room_name1 in rooms_list:
            add_hook("before_open", "ep13_quests4_maurice_meet", scene=room_name1, label="maurice_meet")
    return

label ep13_quests4_maurice_meet:
    $ remove_hook(label="maurice_meet")
    call ep03_dialogues2_college_4()
    call ep03_dialogues2_college_5()

    python:
        set_active("Student12", False, scene="college_coridor5")
        collegeStudent11_Suffix = 1
        add_hook("Teleport_ArtClass", "ep03_dialogues2_college_9", scene="college_coridor5", quest="college_day3")
        add_hook("Teleport_Principal_Secretary", "ep03_dialogues2_college_9", scene="college_coridor8", quest="college_day3")
        add_hook("Teleport_English", "ep03_dialogues2_college_9", scene="college_coridor6", quest="college_day3")

        add_hook("Teleport_Library", "ep13_quests5_college_walk", scene="college_coridor9", quest="college_day3")
        add_hook("Teleport_Gym", "ep13_quests5_college_walk", scene="college_coridor2", quest="college_day3")
        add_hook("Teleport_Algebra", "ep13_quests5_college_walk", scene="college_coridor5", quest="college_day3")

        add_hook("before_open", "ep13_quests5_college_end", scene="college_street", quest="college_day3", once=True)
    call change_scene("college_coridor5", "Fade_long")
    return False

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
    python:
        miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor2", "COLLEGE_Floor1", "COLLEGE_Floor3"]
        remove_hook(label="college_day3")
        add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", quest="day3")
        autorun_to_object("ep03_dialogues4_bike_rental_1", scene="college_street")
        set_object_follow("Teleport_BEACH", scene="map")

        move_object("Sophie", "empty")
        move_object("Sister1", "empty")
        sister1RoomDoorLocked = True
        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True

    call locations_beach1()
    call map_init_beach()
    $ add_hook("before_open", "ep13_quests6_beach1", scene="beach_loungers", quest="day3", once=True)
    $ add_hook("enter_scene", "ep13_quests6_beach1a", scene="beach_loungers", quest="day3", once=True)
    return

label ep13_quests6_beach1:
    call ep03_dialogues4_bike_rental_2()
    $ questHelp("work_1", True)
#    $ autorun_to_object("ep13_quests6_beach1a", scene="beach_loungers")
    call refresh_scene_fade_long()
    return

label ep13_quests6_beach1a:
    $ sophieCallStage = 4
    $ phone_incoming_call("Sophie")
    $ add_hook("phone_close", "ep13_quests6_beach2", scene="phone", once=True, quest="day3")
    return

label ep13_quests6_beach2:
    $ sophieCallStage = 0
    $ questHelp("house_19")
    $ clear_object_follow_all()
    $ set_object_follow("Teleport_Floor1", scene="house_street")
    $ set_object_follow("Teleport_Kitchen", scene="house_floor1")
    $ set_object_follow("Floor1", scene="minimap")
    $ set_object_follow("Teleport_HOUSE", scene="map")
    $ add_hook("before_open", "ep13_quests7_home1", scene="house_street", quest="day3", once=True)

    $ add_hook("before_open", "ep13_quests7_home2", scene="house_floor1", quest="day3", once=True, label="meet_daisy")
    $ add_hook("before_open", "ep13_quests7_home2", scene="house_floor2", quest="day3", once=True, label="meet_daisy")
    $ add_hook("before_open", "ep13_quests7_home2", scene="house_bedroom_mc", quest="day3", label="meet_daisy")

    return

label ep13_quests7_home1:
    # меняем на вечер
    $ remove_hook(label="return_home_process")
    call changeDayTime("evening")
    call ep03_dialogues3_family_evening_1()
    call refresh_scene_fade_long()
    return

label ep13_quests7_home2:
    $ questHelp("house_19", True)
    $ remove_hook(label="meet_daisy")
    call ep03_dialogues3_family_evening_2()
    $ questHelp("house_20")
    $ add_hook("before_open", "ep13_quests7_home3", scene="house_floor2", quest="day3", label="meet_olivia")
    $ add_hook("before_open", "ep13_quests7_home3", scene="house_bedroom_mc", quest="day3", label="meet_olivia")
    $ add_hook("Bed", "ep13_quests7_home4_sleep", scene="house_bedroom_mc", quest="day3")
    $ add_hook("before_open", "ep13_quests7_home3_night", scene="house_bedroom_mc", quest="day3", once=True)

    python:
        clear_object_follow_all()
        set_object_follow("Teleport_Floor2", scene="house_floor1")
        set_object_follow("Teleport_Bedroom_MC", scene="house_floor2")
        set_object_follow("Bed", scene="house_bedroom_mc")
        set_object_follow("House_Bedroom_MC", scene="minimap")

        move_object("Sophie", "house_bedroom_landlord")
        sister1RoomDoorLocked = True
        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True
        remove_hook(label="return_home_process")

    call change_scene("house_floor1", "Fade_long")
    call refresh_scene_fade()
    return False

label ep13_quests7_home3:
    # встречает Оливию с улицы
    $ remove_hook(label="return_home_process")
    $ remove_hook(label="meet_olivia")
    call ep03_dialogues3_family_evening_3()
    call refresh_scene_fade()
    return

label ep13_quests7_home3_night:
    call changeDayTime("night")
    python:
        sister1RoomDoorLocked = True
        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True
        move_object("Sophie", "house_bedroom_landlord")
        move_object("Sister1", "house_sister1")
        move_object("Sister2", "house_sister2")
    return

label ep13_quests7_home4_sleep:
    $ remove_hook()
    $ remove_hook(quest="day3")
    # следующий день!
    $ camera_icon_enabled = False
    $ questHelp("house_20", True)
    call ep03_dialogues3_family_evening_4()
    $ camera_icon_enabled = True
    call changeDayTime("morning")

    # УТРО
    call ep03_dialogues1_family_morning_5()

    python:
        clear_object_follow_all()
        questHelp("house_21")
        map_enabled = False
        add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block", quest="day4")
        miniMapDisabled["HOUSE"] = ["House_Street"]
        sister1RoomDoorLocked = True
        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True
        sophieCallStage = 0
        cynthiaCallStage = 0
        move_object("Sophie", "house_kitchen")
        move_object("Henry", "empty")
        move_object("Sister1", "house_sister1")
        move_object("Sister2", "house_sister2")

        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Floor1", scene="house_floor2")
        set_object_follow("Teleport_Bathroom", scene="house_floor1")
        set_object_follow("Teleport_Kitchen", scene="house_floor1")
        set_object_follow("Floor1", scene="minimap")

        add_hook("before_open", "ep13_quests8_home1_breakfast", scene="house_kitchen", once=True, quest="day4")
    call refresh_scene_fade_long()

    return False

label ep13_quests8_home1_breakfast:
    call ep03_dialogues1_family_morning_6()
    $ clear_object_follow_all()
    $ map_enabled = True
    $ questHelp("house_21", True)
    $ questHelp("work_2")
    $ remove_hook(label="house_block")
    $ miniMapDisabled["HOUSE"] = []
    $ set_object_follow("Teleport_Floor1", scene="house_kitchen")
    $ set_object_follow("Teleport_Street", scene="house_floor1")
    $ set_object_follow("House_Street", scene="minimap")
    $ set_object_follow("Teleport_Map", scene="house_street")
    $ set_object_follow("Teleport_BEACH", scene="map")

    $ add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", quest="day4")
    $ add_hook("before_open", "ep13_quests9_beach1", scene="beach_loungers", once=True, quest="day4")
    call refresh_scene_fade_long()
    return

label ep13_quests9_beach1:
    call ep03_dialogues4_bike_rental_3()
    call beach_loungers_init2()
    call locations_beach2()
    call map_init_park()

    $ remove_hook(label="ep13_quests8_home1_breakfast")

    $ clear_object_follow_all()

    $ questHelp("work_2", True)
    $ houseLifeStage = 1
    $ add_hook("FatherFriend", "ep03_dialogues4_bike_rental_3a", scene="beach_park", label="fatherfriend_park")

    call ep13_quests10_daisy_init()

    call changeDayTime("day")
    call process_change_map_location("PARK")
    call change_scene("beach_park", "Fade_long")
    return

label ep13_quests10_daisy_init:
    $ questHelp("work_3")
    call locations_daisy1()
    call map_init_daisy()
    $ add_hook("before_open", "ep13_quests10_daisy_evening", scene="daisy_street", quest="day4", once=True)
    $ add_hook("Teleport_LivingRoom", "ep13_quests10_daisy1", scene="daisy_street", quest="day4", once=True)
    $ add_hook("enter_scene", "ep03_dialogues3_family_evening_5", scene="daisy_street", quest="day4", once=True)
    $ set_object_follow("Teleport_Map", scene="beach_loungers")
    $ set_object_follow("Teleport_Map", scene="beach_park")
    $ set_object_follow("Teleport_LivingRoom", scene="daisy_street")
    $ set_object_follow("Teleport_DAISY", scene="map")
    return

label ep13_quests10_daisy_evening:
    $ houseLifeStage = 2
    call changeDayTime("evening")
    return

label ep13_quests10_daisy1:
    call ep03_dialogues3_family_evening_6()
    $ questLog(15, True)
    $ questHelp("work_3", True)
    $ clear_object_follow_all()
    $ add_hook("enter_scene", "ep13_quests11_party1", scene="daisy_street", quest="day4", once=True)
    call change_scene("house_street")
    call change_scene("daisy_street")
    call refresh_scene_fade_long()
    return False

label ep13_quests11_party1:
    $ add_hook("phone_close", "ep13_quests11_party2", scene="phone", once=True, quest="college_day3")
    $ seanCallStage = 5
    $ phone_incoming_call("Sean")
    return

label ep13_quests11_party2:
    $ questHelp("college_27")
    call locations_arnie1()
    call map_init_arnie()
    $ set_object_follow("Teleport_Map", scene="daisy_street")
    $ set_object_follow("Teleport_LivingRoom", scene="arnie_street")
    $ set_object_follow("Teleport_ARNIE", scene="map")
    $ add_hook("Teleport_LivingRoom", "ep13_quests11_party3", scene="arnie_street", quest="day4", once=True)

    return

label ep13_quests11_party3:
    $ questHelp("college_27", True)
    call ep03_dialogues2_college_12()
    return False



