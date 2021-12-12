label ep12_quests1_init:
    call phone_instagram2()
    $ phone_instagram_mode = 1

    call changeDayTime("morning")
    #family 
    call ep02_dialogues1_family_1() # момент, на котором закончился 1-й апдейт, комната Барди

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

    $ sister1RoomDoorLocked = True
    $ sister2RoomDoorLocked = True
    $ landLordRoomDoorLocked = True

    $ move_object("Sister2", "college_empty")

    $ set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
    $ add_hook("Teleport_Floor2", "ep12_quests2_bathroom", scene="house_bedroom_mc")
    $ add_hook("before_open", "ep12_quests2_bathroom", scene="house_floor1")

    call refresh_scene_fade()

#    call phone_instagram3()
    return False

label ep12_quests2_bathroom:
    $ remove_hook(label="ep12_quests2_bathroom")
    call ep02_dialogues1_family_1c()

    $ questHelp("house_9", True)
    $ questHelp("house_10")
    $ miniMapEnabledOnly = []
    $ add_hook("before_open", "ep12_quests3_empty", scene="house_bathroom", once=True)
    $ clear_object_follow_all()

    # блокируем выход из дома
    $ add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block")
    $ miniMapDisabled["HOUSE"] = ["House_Street"]

    $ set_object_follow("Teleport_Floor1", scene="house_bathroom")
    $ set_object_follow("Teleport_Kitchen", scene="house_floor1")

    $ add_hook("before_open", "ep12_quests4_kitchen", scene="house_kitchen")

    call change_scene("house_bathroom", "Fade_long")
    return False

label ep12_quests3_empty:
    return False

label ep12_quests4_kitchen:
    $ remove_hook()
    call ep02_dialogues1_family_2() # кухня
    $ clear_object_follow_all()
    $ moneyDisplayEnabled = True
    $ questHelp("house_10", True)
    $ questHelp("college_14")
    $ set_object_follow("Teleport_Street", scene="house_floor1")
    $ set_object_follow("Teleport_Map", scene="house_street")
    $ set_object_follow("Teleport_COLLEGE", scene="map")
    $ miniMapDisabled["HOUSE"] = []
    $ remove_hook(label="house_block")
    $ set_object_follow("Floor1", scene="minimap")

    # init college
    $ add_hook("enter_scene", "ep02_dialogues2_college_1", scene="college_street", once=True)
    $ add_hook("before_open", "ep12_quests5_college", scene="college_coridor1")

    call refresh_scene_fade()
    return False


label ep12_quests5_college: # Барди заходит в колледж холл колледжа у шкафчиков
    $ remove_hook()
    $ clear_object_follow_all()
    call ep02_dialogues2_college_3() # тут же к нему подходит зануда-отличница Сара (student_sarah), в руках папка или учебники
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

    $ add_hook("Teleport_Principal_Secretary", "ep12_quests7_principal_secretary", scene="college_coridor8")
    $ add_hook("Teleport_Library", "ep02_dialogues2_college_3b", scene="college_coridor9", quest="college_day2")

    $ collegeStudent4_Suffix = 2
    $ college_menu_floor2_enabled = False
    call refresh_scene_fade_long()
    return

label ep12_quests6_gymclosed: # 
    sound snd_door_locked1
    pause 1.0
    call ep01_dialogues2_day1_family_1_6()
    return False


label ep12_quests7_principal_secretary:
    $ remove_hook()
    $ clear_object_follow_all()
    $ questHelp("college_16", True)
    call ep02_dialogues2_college_4() # при клике на дверь приемной
    $ questHelp("college_17")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Street"]
    $ college_menu_floor2_enabled = True

    $ set_active("Teleport_Coridor5", True, scene="college_coridor6")
    $ set_active("Teleport_Algebra", True, scene="college_coridor5")
    $ set_active("Teleport_Coridor6", True, scene="college_coridor5")

    $ set_object_follow("Teleport_Coridor9", scene="college_coridor8")
    $ set_object_follow("Teleport_Coridor10", scene="college_coridor9")
    $ set_object_follow("Teleport_Stairs", scene="college_coridor10")

    $ set_object_follow("Teleport_Coridor9", scene="college_coridor8")
    $ set_object_follow("Teleport_Coridor6", scene="college_coridor7")
    $ set_object_follow("Teleport_Coridor5", scene="college_coridor6")
    $ set_object_follow("Teleport_Algebra", scene="college_coridor5")
    $ set_object_follow("ЭТАЖ 2", scene="menu")
    $ set_object_follow("COLLEGE_Floor2", scene="minimap")

    $ add_hook("Teleport_Algebra", "ep12_quests8_algebra", scene="college_coridor5")
    $ set_active("Student12", False, scene="college_coridor5")
    
    $ add_hook("Teleport_Street", "ep02_dialogues2_college_4b", scene="college_coridor1", label="college_street_block", quest="college_day2")
    $ add_hook("Teleport_Gym", "ep02_dialogues2_college_4b", scene="college_coridor2", label="gym_blocked", quest="college_day2")
    

    $ add_hook("Teleport_Principal_Secretary", "ep02_dialogues2_college_3c", scene="college_coridor9", quest="college_day2")
    call refresh_scene_fade()
    return False

label ep12_quests8_algebra:
    $ remove_hook()
    $ questHelp("college_17", True)
    call ep02_dialogues2_college_5() # Барди заходит в кабинет
    fadeblack 1.5
    call college_algebra_init2()
    $ set_active("Teleport_Coridor5", True, scene="college_algebra")
    $ set_var("Teleport_Coridor5", scene="college_algebra", xpos=282, ypos=202)
    $ add_hook("Teleport_Coridor5", "ep02_dialogues2_college_5h", scene="college_algebra", quest="college_day2")
    $ add_hook("Teacher8", "ep12_quests9_algebra2", scene="college_algebra")

    return

label ep12_quests9_algebra2:
    call ep02_dialogues2_college_6() # при клике на Кларк, урок продолжается
    if _return == -1:
        call refresh_scene_fade()
        return False
    $ remove_hook(label="ep12_quests9_algebra2")
    $ questHelp("college_21")
    $ clear_object_follow_all()
    $ set_object_follow("Teleport_Gym", scene="college_coridor2")
    $ add_hook("Teleport_Gym", "ep12_quests10_gym", scene="college_coridor2", quest="college_day2")
    $ set_active("Teleport_Stairs", False, scene="college_coridor2")
    $ miniMapEnabledOnly = ["empty"]

    call change_scene("college_coridor2", "Fade_long")
    return False

label ep12_quests10_gym:
    $ remove_hook()
    call ep02_dialogues2_college_7()
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

    call refresh_scene_fade()
    return False


label ep12_quests11_library:
    $ remove_hook()
    call ep02_dialogues2_college_9()
    $ clear_object_follow_all()
    $ questHelp("college_23", True)
    call changeDayTime("day")
    $ add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", label="college_day2")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor2", "COLLEGE_Floor1", "COLLEGE_Floor3"]

    call ep02_dialogues2_college_10() # при клике на выход из колледжа (после библиотеки)

    $ sophieCallStage = 1
    $ seanCallStage = 0
    $ add_hook("enter_scene", "ep12_quests12_phone", scene="college_street")
    call change_scene("college_street", "Fade_long")
    return False

label ep12_quests12_phone:
    $ remove_hook()
    $ add_hook("phone_close", "ep12_quests13_phone_after", scene="phone", once=True)
    $ phone_incoming_call("Sophie")


    return False

label ep12_quests13_phone_after:
    if questHelpGetStatus("sean_1") == 0:
        $ questHelp("sean_1", False)
    $ questHelp("sean_2")
    $ remove_hook(label="sean_visit")

    $ map_enabled = True
    $ set_object_follow("Teleport_Map", scene="college_street")
    $ set_object_follow("Teleport_HOUSE_FRIEND", scene="map")
    $ set_object_follow("Teleport_LivingRoom", scene="housefriend_street")
    $ autorun_to_object("ep02_dialogues3_sean_1", scene="housefriend_street")
    $ add_hook("Teleport_LivingRoom", "ep12_quests14_sean", scene="housefriend_street")

    return

label ep12_quests14_sean:
    $ remove_hook()
    $ clear_object_follow_all()
    call ep02_dialogues3_sean_2()
#    call changeDayTime("evening")
    call change_scene("housefriend_livingroom", "Fade_long")
    return False


#