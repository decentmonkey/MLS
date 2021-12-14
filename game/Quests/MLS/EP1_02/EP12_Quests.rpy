label ep12_quests1_init:
    call phone_instagram2() from _rcall_phone_instagram2
    $ phone_instagram_mode = 1

    call changeDayTime("morning") from _rcall_changeDayTime_12
    #family
    call ep02_dialogues1_family_1() from _rcall_ep02_dialogues1_family_1 # момент, на котором закончился 1-й апдейт, комната Барди

    # убираем залипшие квесты
    python:
        if questHelpGetStatus("house_7") == 0:
            questHelpRemove("house_7")
        if questHelpGetStatus("house_8") == 0:
            questHelpRemove("house_8")
        if questHelpGetStatus("college_4") == 0:
            questHelpRemove("college_4")

    $ cynthiaCallStage = 0
    $ questHelp("house_9")
    $ miniMapDisabled["HOUSE"] = []
    $ miniMapEnabledOnly = ["Floor1"]
    $ set_object_follow("Floor1", scene="minimap")
    $ map_enabled = False

    $ sister1RoomDoorLocked = True
    $ sister2RoomDoorLocked = True
    $ landLordRoomDoorLocked = True

    $ move_object("Sister2", "college_empty")

    $ set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
    $ add_hook("Teleport_Floor2", "ep12_quests2_bathroom", scene="house_bedroom_mc", quest="day2")
    $ add_hook("before_open", "ep12_quests2_bathroom", scene="house_floor1", quest="day2")

    call refresh_scene_fade() from _rcall_refresh_scene_fade_16

#    call phone_instagram3()
    return False

label ep12_quests2_bathroom:
    $ remove_hook(label="ep12_quests2_bathroom")
    call ep02_dialogues1_family_1c() from _rcall_ep02_dialogues1_family_1c

    $ questHelp("house_9", True)
    $ questHelp("house_10")
    $ miniMapEnabledOnly = []
    $ add_hook("before_open", "ep12_quests3_empty", scene="house_bathroom", once=True, quest="day2")
    $ clear_object_follow_all()

    # блокируем выход из дома
    $ add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block", quest="day2")
    $ miniMapDisabled["HOUSE"] = ["House_Street"]

    $ set_object_follow("Teleport_Floor1", scene="house_bathroom")
    $ set_object_follow("Teleport_Kitchen", scene="house_floor1")
    $ set_object_follow("Floor1", scene="minimap")

    $ add_hook("before_open", "ep12_quests4_kitchen", scene="house_kitchen", quest="day2")

    call change_scene("house_bathroom", "Fade_long") from _rcall_change_scene_117
    return False

label ep12_quests3_empty:
    return False

label ep12_quests4_kitchen:
    $ remove_hook()
    call ep02_dialogues1_family_2() from _rcall_ep02_dialogues1_family_2 # кухня
    $ clear_object_follow_all()
    $ moneyDisplayEnabled = True
    $ questHelp("house_10", True)
    $ questHelp("college_14")
    $ questHelpDesc("house_desc4", "house_desc7")
    $ questHelpDesc("house_desc5", "house_desc7")

    $ map_enabled = True
    $ set_object_follow("Teleport_Street", scene="house_floor1")
    $ set_object_follow("Teleport_Map", scene="house_street")
    $ set_object_follow("Teleport_COLLEGE", scene="map")
    $ miniMapDisabled["HOUSE"] = []
    $ remove_hook(label="house_block")
    $ set_object_follow("House_Street", scene="minimap")

    # init college
    $ add_hook("enter_scene", "ep02_dialogues2_college_1", scene="college_street", once=True, quest="day2")
    $ add_hook("before_open", "ep12_quests5_college", scene="college_coridor1", quest="day2")

    call refresh_scene_fade() from _rcall_refresh_scene_fade_17
    return False


label ep12_quests5_college: # Барди заходит в колледж холл колледжа у шкафчиков
    $ remove_hook()
    $ clear_object_follow_all()
    call ep02_dialogues2_college_3() from _rcall_ep02_dialogues2_college_3 # тут же к нему подходит зануда-отличница Сара (student_sarah), в руках папка или учебники
    $ set_active("Student3", False, scene="college_coridor1")
    $ set_active("Student2", False, scene="college_coridor1")
    $ set_active("Student8", False, scene="college_coridor3")
    $ set_active("Student14", False, scene="college_coridor6")
    $ questHelp("college_14", True)
    $ questHelp("college_16")
    $ set_active("Teleport_Coridor2", True, scene="college_coridor3")
    $ set_active("Teleport_Gym", True, scene="college_coridor2")
    $ set_active("Teleport_Stairs", True, scene="college_coridor2")
    $ set_active("Teleport_Stairs", True, scene="college_coridor7")
    $ set_active("Teleport_Coridor6", True, scene="college_coridor7")
    $ set_active("Teleport_Coridor7", True, scene="college_coridor6")
    $ set_active("Teleport_Coridor10", True, scene="college_roof")
    $ set_active("Teleport_Stairs", True, scene="college_coridor10")
    $ set_active("Teleport_Coridor9", True, scene="college_coridor10")
    $ set_active("Teleport_Coridor10", True, scene="college_coridor9")
#    $ set_active("Teleport_Teachers", True, scene="college_coridor9")
    $ set_active("Teleport_Coridor8", True, scene="college_coridor9")
    $ set_active("Teleport_Coridor9", True, scene="college_coridor8")
    $ set_active("Teleport_Library", True, scene="college_coridor9")
    $ set_active("Teleport_Coridor1", True, scene="college_coridor3")
    $ set_active("Teleport_Principal_Secretary", True, scene="college_coridor8")



    $ set_var("Student4", zorder=12, scene_name="college_coridor2")
    $ set_var("Teleport_Floor2", ypos = 130, scene="college_coridor3")
    $ remove_hook(label="ep1_college3_english_location")
    $ add_hook("Teleport_Gym", "ep02_dialogues2_college_3a", scene="college_coridor2", label="gym_blocked", quest="college_day2")
    $ add_hook("Teleport_English", "ep12_quests6_gymclosed", scene="college_coridor6", label="english_blocked", quest="college_day2")
    $ add_hook("Teleport_Street", "ep01_dialogues3_day2_college_2", scene="college_coridor1", label="college_street_block", quest="college_day2")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor2", "COLLEGE_Street"]

    $ set_object_follow("Teleport_Stairs", scene="college_coridor1")
    $ set_object_follow("Teleport_Floor2", scene="college_coridor3")
    $ set_object_follow("Teleport_Coridor9", scene="college_coridor10")
    $ set_object_follow("Teleport_Coridor8", scene="college_coridor9")
    $ set_object_follow("Teleport_Principal_Secretary", scene="college_coridor8")
    $ set_object_follow("ЭТАЖ 3", scene="menu")
    $ set_object_follow("COLLEGE_Floor3", scene="minimap")

    $ add_hook("Teleport_Principal_Secretary", "ep12_quests7_principal_secretary", scene="college_coridor8", quest="day2")
    $ add_hook("Teleport_Library", "ep02_dialogues2_college_3b", scene="college_coridor9", quest="college_day2")

    $ collegeStudent4_Suffix = 2
    $ college_menu_floor2_enabled = False
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_12
    return

label ep12_quests6_gymclosed: #
    sound snd_door_locked1
    pause 1.0
    call ep01_dialogues2_day1_family_1_6() from _rcall_ep01_dialogues2_day1_family_1_6_3
    return False


label ep12_quests7_principal_secretary:
    $ remove_hook()
    $ clear_object_follow_all()
    $ questHelp("college_16", True)
    call ep02_dialogues2_college_4() from _rcall_ep02_dialogues2_college_4 # при клике на дверь приемной
    $ questHelp("college_17")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Street"]
    $ college_menu_floor2_enabled = True

    $ set_active("Teleport_Coridor5", True, scene="college_coridor6")
    $ set_active("Teleport_Algebra", True, scene="college_coridor5")
    $ set_active("Teleport_Coridor6", True, scene="college_coridor5")
    $ set_active("Teleport_Coridor8", True, scene="college_principal_secretary")
    
    $ add_hook("Principal_Secretary", "ep02_dialogues2_college_4b", scene="college_principal_secretary", quest="day2")

    $ set_object_follow("Teleport_Coridor9", scene="college_coridor8")
    $ set_object_follow("Teleport_Coridor10", scene="college_coridor9")
    $ set_object_follow("Teleport_Stairs", scene="college_coridor10")

    $ set_object_follow("Teleport_Coridor9", scene="college_coridor8")
    $ set_object_follow("Teleport_Coridor6", scene="college_coridor7")
    $ set_object_follow("Teleport_Coridor5", scene="college_coridor6")
    $ set_object_follow("Teleport_Algebra", scene="college_coridor5")
    $ set_object_follow("ЭТАЖ 2", scene="menu")
    $ set_object_follow("COLLEGE_Floor2", scene="minimap")

    $ add_hook("Teleport_Algebra", "ep12_quests8_algebra", scene="college_coridor5", quest="college_day2")
    $ set_active("Student12", False, scene="college_coridor5")

    $ add_hook("Teleport_Street", "ep02_dialogues2_college_4b", scene="college_coridor1", label="college_street_block", quest="college_day2")
    $ add_hook("Teleport_Gym", "ep02_dialogues2_college_4b", scene="college_coridor2", label="gym_blocked", quest="college_day2")


    $ add_hook("Teleport_Principal_Secretary", "ep02_dialogues2_college_3c", scene="college_coridor9", quest="college_day2")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_18
    return False

label ep12_quests8_algebra:
    $ remove_hook()
    $ questHelp("college_17", True)
    $ questHelpDesc("college_desc6")
    call ep02_dialogues2_college_5() from _rcall_ep02_dialogues2_college_5 # Барди заходит в кабинет
    fadeblack 1.5
    call college_algebra_init2() from _rcall_college_algebra_init2
    $ set_active("Teleport_Coridor5", True, scene="college_algebra")
    $ set_var("Teleport_Coridor5", scene="college_algebra", xpos=282, ypos=202)
    $ add_hook("Teleport_Coridor5", "ep02_dialogues2_college_5h", scene="college_algebra", quest="college_day2")
    $ add_hook("Teacher8", "ep12_quests9_algebra2", scene="college_algebra", quest="day2")

    return

label ep12_quests9_algebra2:
    call ep02_dialogues2_college_6() from _rcall_ep02_dialogues2_college_6 # при клике на Кларк, урок продолжается
    if _return == -1:
        call refresh_scene_fade() from _rcall_refresh_scene_fade_19
        return False
    $ remove_hook(label="ep12_quests9_algebra2")
    $ questHelp("college_21")
    $ clear_object_follow_all()
    $ set_object_follow("Teleport_Gym", scene="college_coridor2")
    $ add_hook("Teleport_Gym", "ep12_quests10_gym", scene="college_coridor2", quest="college_day2")
    $ set_active("Teleport_Stairs", False, scene="college_coridor2")
    $ miniMapEnabledOnly = ["empty"]

    call change_scene("college_coridor2", "Fade_long") from _rcall_change_scene_118
    return False

label ep12_quests10_gym:
    $ remove_hook()
    call ep02_dialogues2_college_7() from _rcall_ep02_dialogues2_college_7
    $ add_hook("Teleport_Gym", "ep02_dialogues2_college_8a", scene="college_coridor2", quest="college_day2")
    $ add_hook("Teleport_Street", "ep02_dialogues2_college_8a", scene="college_coridor1", label="college_street_block", quest="college_day2")
    $ add_hook("Teleport_Principal_Secretary", "ep02_dialogues2_college_8a", scene="college_coridor8", quest="college_day2")
    $ add_hook("Teleport_Algebra", "ep02_dialogues2_college_8a", scene="college_coridor5", quest="college_day2")
    $ add_hook("Teleport_English", "ep02_dialogues2_college_8a", scene="college_coridor6", quest="college_day2")

    $ add_hook("Teleport_Library", "ep12_quests11_library", scene="college_coridor9", quest="college_day2")

    $ autorun_to_object("ep02_dialogues2_college_8a", scene="college_coridor2")

    $ set_active("Teleport_Stairs", True, scene="college_coridor2")
    $ miniMapEnabledOnly = []

    $ clear_object_follow_all()
    $ set_object_follow("ЭТАЖ 3", scene="menu")
    $ set_object_follow("COLLEGE_Floor3", scene="minimap")
    $ set_object_follow("Teleport_Stairs", scene="college_coridor2")
    $ set_object_follow("Teleport_Floor2", scene="college_coridor3")
    $ set_object_follow("Teleport_Coridor9", scene="college_coridor10")
    $ set_object_follow("Teleport_Library", scene="college_coridor9")


    $ questHelp("college_21", True)
    $ questHelp("college_23")

    call refresh_scene_fade() from _rcall_refresh_scene_fade_20
    return False


label ep12_quests11_library:
    $ remove_hook()
    call ep02_dialogues2_college_9() from _rcall_ep02_dialogues2_college_9
    $ clear_object_follow_all()
    $ questHelp("college_23", True)
    call changeDayTime("day") from _rcall_changeDayTime_13
    $ add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", quest="college_day2")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor2", "COLLEGE_Floor1", "COLLEGE_Floor3"]

    call ep02_dialogues2_college_10() from _rcall_ep02_dialogues2_college_10 # при клике на выход из колледжа (после библиотеки)

    $ sophieCallStage = 1
    $ seanCallStage = 0
    $ add_hook("enter_scene", "ep12_quests12_phone", scene="college_street", quest="day2")
    call change_scene("college_street", "Fade_long") from _rcall_change_scene_119
    return False

label ep12_quests12_phone:
    $ remove_hook()
    $ add_hook("phone_close", "ep12_quests13_phone_after", scene="phone", once=True, quest="day2")
    $ phone_incoming_call("Sophie")


    return False

label ep12_quests13_phone_after:
    if questHelpGetStatus("sean_1") == 0:
        $ questHelp("sean_1", False)
    $ questHelp("sean_2")
    $ remove_hook(label="sean_visit")

    # инитим Шона
    $ map_enabled = True
    $ homeButtonEnabled = True
    $ set_object_follow("Teleport_Map", scene="college_street")
    $ set_object_follow("Teleport_HOUSE_FRIEND", scene="map")
    $ set_object_follow("Teleport_LivingRoom", scene="housefriend_street")
#    $ autorun_to_object("ep02_dialogues3_sean_1", scene="housefriend_street")
    $ add_hook("Teleport_LivingRoom", "ep12_quests14_sean", scene="housefriend_street", quest="day2")

    # инитим дом
    $ add_hook("before_open", "ep12_quests15_home", scene="house_floor1", quest="day2")
    $ miniMapDisabled["HOUSE"] = ["House_Bedroom_MC", "Floor2"]

    call ep02_dialogues3_sean_1() from _rcall_ep02_dialogues3_sean_1

    return

label ep12_quests14_sean:
    $ remove_hook()
    $ clear_object_follow_all()
    call ep02_dialogues3_sean_2() from _rcall_ep02_dialogues3_sean_2
    $ move_object("Mother_Friend", "empty")
    call housefriend_livingroom_init2() from _rcall_housefriend_livingroom_init2
    $ add_hook("Teleport_Street", "ep02_dialogues3_sean_2a", scene="housefriend_livingroom", quest="day2")
    $ add_hook("TV", "ep02_dialogues3_sean_2b", scene="housefriend_livingroom", quest="day2")
    $ add_hook("Teleport_Kitchen", "ep02_dialogues3_sean_2c", scene="housefriend_livingroom", once=True, quest="day2")
    $ add_hook("Teleport_Room", "ep02_dialogues3_sean_2d", scene="housefriend_livingroom", once=True, quest="day2")
    $ add_hook("before_open", "ep12_quests14a_sean", scene="housefriend_room", once=True, quest="day2")
    $ add_hook("enter_scene", "ep02_dialogues3_sean_2c1", scene="housefriend_bedroom_parents", once=True, quest="day2")
    call change_scene("housefriend_livingroom", "Fade_long") from _rcall_change_scene_120
    return False

label ep12_quests14a_sean:
    call ep02_dialogues3_sean_3() from _rcall_ep02_dialogues3_sean_3
    call changeDayTime("evening") from _rcall_changeDayTime_14
    $ focus_map("Teleport_HOUSE", "ep02_dialogues3_sean_4")
    $ questHelp("sean_2", True)
    $ questHelp("house_11")
    $ seanCallStage = 3
    call change_scene("housefriend_street", "Fade_long") from _rcall_change_scene_121
    return False

label ep12_quests14b_sean_afterphone:
    call ep02_dialogues3_sean_5c() from _rcall_ep02_dialogues3_sean_5c
    $ questHelp("sean_3")
    $ questHelpDesc("sean_desc1", "sean_desc2")
    return

label ep12_quests15_home:
    $ remove_hook()
    $ clear_object_follow_all()
    $ unfocus_map()
    $ sophieCallStage = 0
    call ep02_dialogues4_family_evening_1() from _rcall_ep02_dialogues4_family_evening_1
    call ep02_dialogues4_family_evening_2() from _rcall_ep02_dialogues4_family_evening_2
    $ add_hook("Teleport_Sister1", "ep02_dialogues4_family_evening_3", scene="house_floor2", quest="day2")
    $ add_hook("Teleport_Sister2", "ep02_dialogues4_family_evening_4", scene="house_floor2", quest="day2")
    $ add_hook("before_open", "ep12_quests16_home", scene="house_bedroom_mc", quest="day2")

    $ add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block", quest="day2")
    $ miniMapDisabled["HOUSE"] = ["House_Street"]

    $ move_object("Sophie", "empty")
    $ move_object("Henry", "empty")
    $ move_object("Sister1", "house_sister1")
    $ move_object("Sister2", "house_sister2")
    $ questHelp("house_11", True)
    $ questHelp("house_12")

    $ sister1RoomDoorLocked = True
    $ sister2RoomDoorLocked = True
    $ landLordRoomDoorLocked = True

    $ set_object_follow("Teleport_Floor2", scene="house_floor1")
    $ set_object_follow("Teleport_Bedroom_MC", scene="house_floor2")
    $ set_object_follow("House_Bedroom_MC", scene="minimap")

    call change_scene("house_livingroomhall", "Fade_long") from _rcall_change_scene_122
    return False

label ep12_quests16_home:
    $ remove_hook()
    call ep02_dialogues4_family_evening_5() from _rcall_ep02_dialogues4_family_evening_5
    call change_scene("house_floor1", "Fade_long") from _rcall_change_scene_123
    $ remove_hook(label="ep02_dialogues4_family_evening_3")
    $ add_hook("Teleport_Sister2", "ep02_dialogues4_family_evening_6", scene="house_floor2", quest="day2")
    $ move_object("Sister1", "empty")
    $ add_hook("before_open", "ep12_quests17_home", scene="house_bedroom_mc", quest="day2")
#    $ questHelp("house_12", True)
    return False

label ep12_quests17_home:
    $ remove_hook()
    $ clear_object_follow_all()
    $ miniMapEnabledOnly = ["none"]
    call locations_init2() from _rcall_locations_init2
    call ep02_dialogues4_family_evening_7() from _rcall_ep02_dialogues4_family_evening_7
    if _return == -1: # просто смотрим инстаграм Эмили
        $ questHelp("house_12", True)
        $ questHelp("house_13")
        $ add_hook("Teleport_Bedroom_MC", "ep02_dialogues4_family_evening_7b", scene="house_bedroom_mc_onbed", quest="day2", label="emily_instagram_block")
        call phone_instagram3() from _rcall_phone_instagram3
        $ add_hook("instagram", "ep12_quests17a_home", scene="phone", quest="day2")
        call change_scene("house_bedroom_mc_onbed", "Fade_long") from _rcall_change_scene_124
        return False
    if _return == 1: # Эмили нам звонит
        $ add_hook("enter_scene", "ep12_quests18_home", scene="house_bedroom_mc_onbed", once=True, quest="day2")
        call change_scene("house_bedroom_mc_onbed", "Fade_long") from _rcall_change_scene_125
        return False


    return False

label ep12_quests17a_home: # проверил инстаграм
    if phone_instagram_current_name != "Emily":
        return
    $ remove_hook()
    $ questHelp("house_13", True)
    $ questHelpDesc("college_desc11")
    $ remove_hook(label="emily_instagram_block")
    $ add_hook("phone_close", "ep12_quests19_home", scene="phone", once=True, quest="day2")

    return

label ep12_quests18_home:
    call phone_contact5() from _rcall_phone_contact5
    $ emilyCallStage = 1
    $ phone_incoming_call("Emily")
    bardi_t "Интересно, кто это там написал... Посмотрим..."
    $ add_hook("phone_close", "ep12_quests18a_home", scene="phone", once=True, quest="day2")
    return

label ep12_quests18a_home:
    pause 1.0
    call ep02_dialogues4_family_evening_7c() from _rcall_ep02_dialogues4_family_evening_7c
    $ emilyCallStage = 0
    $ questHelp("house_12", True)
    $ questHelp("house_13")
    $ add_hook("Teleport_Bedroom_MC", "ep02_dialogues4_family_evening_7b", scene="house_bedroom_mc_onbed", quest="day2", label="emily_instagram_block")
    call phone_instagram3() from _rcall_phone_instagram3_1
    $ add_hook("instagram", "ep12_quests17a_home", scene="phone", quest="day2")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_21
    return False


label ep12_quests19_home: # продолжаем сюжет после Эмили
    $ questLog(10, True)
    pause 1.0
    $ miniMapEnabledOnly = []
    call ep02_dialogues4_family_evening_9() from _rcall_ep02_dialogues4_family_evening_9
    call refresh_scene_fade() from _rcall_refresh_scene_fade_22
    call change_scene("house_bedroom_mc") from _rcall_change_scene_126
    $ add_hook("enter_scene", "ep12_quests19a_home", scene="house_bedroom_mc_onbed", quest="day2")
    call change_scene("house_bedroom_mc_onbed", "Fade_long", False) from _rcall_change_scene_127
    return

label ep12_quests19a_home:
    $ remove_hook()
    $ sophieCallStage = 2
    $ phone_incoming_call("Sophie")
    call ep02_dialogues4_family_evening_9a() from _rcall_ep02_dialogues4_family_evening_9a
    $ add_hook("phone_close", "ep12_quests19b_home", scene="phone", once=True, quest="day2")
    return

label ep12_quests19b_home:
    pause 1.0
    $ questHelp("house_14")
    call ep02_dialogues4_family_evening_11() from _rcall_ep02_dialogues4_family_evening_11
    if _return == -1:
        $ questHelp("house_14", False)
        call ep02_dialogues4_family_evening_12b() from _rcall_ep02_dialogues4_family_evening_12b
    else:
        $ questHelp("house_14", True)
        $ questHelpDesc("house_desc2", "house_desc8")

    call ep02_dialogues4_family_evening_13() from _rcall_ep02_dialogues4_family_evening_13
    if _return == -1:
        call refresh_scene_fade() from _rcall_refresh_scene_fade_23
        call change_scene("house_floor1", "Fade_long") from _rcall_change_scene_128
        $ questHelp("house_15", False)
    else:
        call refresh_scene_fade() from _rcall_refresh_scene_fade_24
        call change_scene("house_kitchen", "Fade_long") from _rcall_change_scene_129
        $ questHelp("house_15", True)
        $ questHelpDesc("house_desc6", "house_desc9")


    call changeDayTime("night") from _rcall_changeDayTime_15
    $ move_object("Sister1", "house_sister1")

    $ sister1RoomDoorLocked = True
    $ sister2RoomDoorLocked = True
    $ landLordRoomDoorLocked = True

    $ questHelp("house_16")
    $ add_hook("Bed", "ep12_quests20_home", scene="house_bedroom_mc", quest="day2")
    return

label ep12_quests20_home:
    call ep01_dialogues2_day1_family_3() from _rcall_ep01_dialogues2_day1_family_3_2
    if _return == False:
        return False
    call ep02_dialogues4_family_evening_14() from _rcall_ep02_dialogues4_family_evening_14
    $ remove_hook(label="college_day2")
    $ remove_hook(label="day2")
    jump end_update

#    return False


#
