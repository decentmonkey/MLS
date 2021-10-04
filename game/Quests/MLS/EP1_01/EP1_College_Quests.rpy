default ep1_college_talk_sean_agree = False
default ep1_college5_college_init_sean_Flag = False

label ep1_college_open:
    $ questHelp("college_1", True)
    $ questHelp("college_2")
    return

label ep1_college_sean: # встреча с Шоном
    $ remove_hook(label="college_sean")
    $ remove_hook(label="day1_morning")
    if ep1_intro_quests6_cynthia_bathroom_Flag == False:
        $ questHelp("college_4", False)
        $ questHelp("house_3", False)
    $ clear_object_follow_all()


    $ questHelp("college_2", True)
    $ questHelp("college_3")

    call ep01_dialogues3_day2_college_1()

    $ move_object("Friend_Bardie", "college_empty")

    # добавляем контакт Шона
    call phone_contacts2()
    # добавляем контакт Синтии
    call phone_contacts3()

    # выключаем все указатели в колледже
    $ set_active(False, group="teleports", scene="college_coridor1", recursive=True)

    # выключаем студентов в коридоре
    $ set_active(False, group="students", scene="college_coridor1")

    $ miniMapEnabledOnly = ["none"]

    # включаем указатель к лестнице
    $ set_active("Teleport_Stairs", True, scene="college_coridor1")
    $ set_active("Teleport_Street", True, scene="college_coridor1")
    $ set_active("Teleport_LockerMC", True, scene="college_coridor1")
    $ set_active("Teleport_Coridor1", True, scene="college_coridor1_locker_mc")
    $ add_hook("Teleport_Stairs", "ep1_college1_principal_search", scene="college_coridor1")
    $ add_hook("Teleport_Street", "ep01_dialogues3_day2_college_2", scene="college_coridor1", label="day1_college")
    $ add_hook("Teleport_LockerMC", "ep01_dialogues3_day2_college_4", scene="college_coridor1", label="day1_college_locker")


    # коридор у входа к секретарю
    $ autorun_to_object("ep01_dialogues3_day2_college_4a", scene="college_coridor8")
    $ set_active("Teleport_Principal_Secretary", True, scene="college_coridor8")

    $ questHelp("college_6")
    $ set_object_follow("Teleport_Stairs", scene="college_coridor1")
    $ set_object_follow("Teleport_Principal_Secretary", scene="college_coridor8")
    $ add_hook("Teleport_Principal_Secretary", "ep1_college2_principal_secretary", scene="college_coridor8")

    call change_scene("college_coridor1", "Fade_long", False)
    return False

label ep1_college1_principal_search: # приходим в локацию
    $ remove_hook()
    sound run_stairs_floor
    fadeblack 2.0
    call change_scene("college_coridor8", "Fade_long", False)
    return False

label ep1_college2_principal_secretary: # идем к секретарю
    $ remove_hook()
    $ questHelp("college_6", True)
    call ep01_dialogues3_day2_college_5()
    $ questHelp("college_7")
    call college_life_forced()
    $ remove_hook(label="day1_college_locker")

    $ miniMapEnabledOnly = []
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor3", "COLLEGE_Street"]

    $ set_active("Student8", False, scene="college_coridor3")
    $ set_active("Student14", False, scene="college_coridor6")
    $ set_active("Teleport_Floor2", True, scene="college_coridor3")

    $ clear_object_follow_all()
    $ set_object_follow("Teleport_Stairs", scene="college_coridor1")
    $ set_object_follow("Teleport_Floor2", scene="college_coridor3")
    $ set_object_follow("Teleport_English", scene="college_coridor6")

    $ add_hook("Teleport_Floor2", "ep1_college3_english_location", scene="college_coridor3", label="ep1_college3_english_location")
    $ add_hook("before_open", "ep1_college3_english_location", scene="college_coridor7", label="ep1_college3_english_location")

    $ add_hook("Teleport_Street", "ep01_dialogues3_day2_college_7", scene="college_coridor1", label="day1_college")


    call change_scene("college_coridor1", "Fade_long")
    return False

label ep1_college3_english_location: # у кабинета английского
    $ remove_hook()
    call ep01_dialogues3_day2_college_8() # ищет английский

    $ questHelp("college_7", True)
    $ questHelp("college_8")
    $ add_hook("Teleport_English", "ep1_college3_english_cabinet", scene="college_coridor6", label="ep1_college3_english_cabinet")
    $ miniMapEnabledOnly = ["none"]

    $ set_active("Teleport_English", True, scene="college_coridor6")
    $ autorun_to_object("ep01_dialogues3_day2_college_8a", scene="college_coridor6")
    call change_scene("college_coridor6", "Fade_long")
    return False

label ep1_college3_english_cabinet:
    $ remove_hook()
    $ questHelp("college_8", True)
    $ questHelp("college_8a")
#    python:
#        set_var("MC", selectable=False, scene="college_english")
#        set_var("Visitor1", selectable=False, scene="college_english")
#        set_var("Visitor2", selectable=False, scene="college_english")
#        set_var("Visitor3", selectable=False, scene="college_english")
#        set_var("Visitor4", selectable=False, scene="college_english")
#        set_var("Visitor1", selectable=False, scene="college_english")
#        set_var("Visitor6", selectable=False, scene="college_english")
#        set_var("Visitor7", selectable=False, scene="college_english")
#        set_var("Visitor8", selectable=False, scene="college_english")
#        set_var("Visitor9", selectable=False, scene="college_english")
    $ set_object_follow("Visitor5", scene="college_english")
    $ add_hook("Visitor1", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("Visitor2", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("Visitor3", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("Visitor4", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("Visitor5", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("Visitor6", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("Visitor7", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("Visitor8", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("Visitor9", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("MC", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    $ add_hook("Teacher", "ep1_college4_english_student_harry", scene="college_english", label="ep1_college4_english_student_harry")
    call ep01_dialogues3_day2_college_9()
    call change_scene("college_english", "Fade_long")
    return False

label ep1_college4_english_student_harry:
    $ remove_hook(label="ep1_college4_english_student_harry")
    $ clear_object_follow_all()
    $ questHelp("college_8a", True)
    call ep01_dialogues3_day2_college_10()
    call changeDayTime("day")

    $ miniMapEnabledOnly = []
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor1", "COLLEGE_Floor2", "COLLEGE_Floor3"]

    $ move_object("Friend_Bardie", "housefriend_room")
    $ add_hook("enter_scene", "ep1_college5_college_end", scene="college_street")
    call change_scene("college_street", "Fade_long")


    return False

label ep1_college5_college_end:
    $ remove_hook()
    $ remove_hook(label="day1_college")
    $ questHelp("college_13", True)
    call ep1_home_quests1_init()

    $ add_hook("enter_scene", "ep1_college5_college_end2_cynthia_call", scene="house_street", label="ep1_college5_college_end2_cynthia_call", once=True)

#    $ add_hook("call_contact_end_close", "ep1_college5_college_end2", scene="phone", label="ep1_college5_college_end2", once=True)

    call ep01_dialogues3_day2_college_11()

    # блокируем колледж
    $ add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", label="day1_college")

    $ seanCallStage = 1
    $ cynthiaCallStage = 1
    $ phone_incoming_call("Sean")
#    $ add_hook("call_contact_end_close", "ep1_college5_college_init_sean", scene="phone", label="ep1_college5_college_init_sean")
#    $ add_hook("call_contact_end_close", "ep1_college5_college_end_cynthia_call", scene="phone", label="ep1_college5_college_end_cynthia_call")
#    call ep1_college5_college_init_sean() - делается в звонке

    $ set_object_follow("Teleport_Map", scene="college_street")

#    call refresh_scene_fade()
    return

label ep1_college5_college_end2_cynthia_call:
    $ phone_incoming_call("Cynthia")
    return


label ep1_college5_college_init_sean:
    # инитим Шона
    if ep1_college_talk_sean_agree == True:
        $ questHelp("sean_1")
        $ add_hook("call_contact_end_close", "ep01_dialogues3_day2_college_12", scene="phone", label="ep01_dialogues3_day2_college_12", once=True)
#        $ autorun_to_object("ep01_dialogues3_day2_college_12", scene=scene_name)
#        call refresh_scene_fade()
    if ep1_college5_college_init_sean_Flag == True:
        return
    $ ep1_college5_college_init_sean_Flag = True
    $ map_objects["Teleport_HOUSE_FRIEND"] = {"text" : t_("ДОМ ШОНА"), "xpos" : 1303, "ypos" : 318, "base" : "map_marker", "state" : "visible"}
    $ autorun_to_object("ep01_dialogues3_day2_college_13", scene="housefriend_street")
    $ add_hook("enter_scene", "ep01_dialogues3_day2_college_12", scene="house_street", label="sean_visit", once=True)
#    $ focus_map("HOUSE_FRIEND", "ep01_dialogues3_day2_college_12a")
    $ set_object_follow("Teleport_LivingRoom", scene="housefriend_street")
    $ add_hook("Teleport_LivingRoom", "ep1_college5_college_sean_home", scene="housefriend_street", label="sean_visit")
#    call refresh_scene_fade()
    return

label ep1_college5_college_sean_home:
    $ seanCallStage = 0
    $ remove_hook(label="sean_visit")
    call ep01_dialogues3_day2_college_14()
    $ set_active("Teleport_LivingRoom", False, scene="housefriend_room")
    $ move_object("Friend_Bardie", "housefriend_room")
    $ houseFriendRoom_Friend_BardieSuffix1 = 3
#    $ phoneEnabled = False
#    $ set_var("Friend_Bardie", base="HouseFriend_Room[housefriend_room_forced_evening_time_suffix]_Friend_Bardie_[houseFriendRoom_Friend_BardieSuffix1]", scene="housefriend_room")
    $ add_hook("Friend_Bardie", "ep1_college5_college_sean_home2", scene="housefriend_room")
    call change_scene("housefriend_room", "Fade_long")
    return False

label ep1_college5_college_sean_home2:
    $ remove_hook()
    call ep01_dialogues3_day2_college_14a()
    call changeDayTime("evening")
#    $ phoneEnabled = True
    call ep01_dialogues3_day2_college_15()
    call sophie_chat1()
#    $ set_var("Friend_Bardie", base="HouseFriend_Room[day_suffix]_Friend_Bardie_[houseFriendRoom_Friend_BardieSuffix1]", scene="housefriend_room")
    $ set_active("Teleport_LivingRoom", True, scene="housefriend_room")
    $ add_hook("Teleport_LivingRoom", "ep01_dialogues2_day1_family_1_12", label="sean_block")
    $ questHelp("sean_1", True)
    $ questHelpDesc("sean_desc1")
    call change_scene("housefriend_street", "Fade_long")
    return False





#
