default ep15_update_init_flag = False

default ep15_bike_rental_scene = 0
default ep15_quests10_sister3_Olivia_phone_day = 0
default ep15_quests10_sister3_Olivia_day = 0
default ep15_quests9_daisy3_Flag = False
default ep15_quests9_daisy3_refuse_day = 0
default ep05_dialogues2_family_daisy_visit_day = 0
default ep15_sleep_regular_dialogue_skip_day = 0
default ep15_quests12_init_sophie_flag = False

label ep15_update_init:
    if ep15_update_init_flag == True:
        return

    python:
        set_room_parent("house_bedroom_mc_onbed", "house_bedroom_mc")

    call object_follow_array_init()
    $ questHelp("house_29", True)
    call ep05_dialogues4_college_emily_1()

    call locations_init2()
    call house_bedroom_mc_onbed_init2()

    $ house_bedroom_mc_onbed_suffix = 2
    call change_scene("house_bedroom_mc_onbed")
    call process_change_map_location("HOUSE")
    call changeDayTime("morning")
    $ questHelp("house_30")
    $ phone_focus_icon(False)
    $ map_enabled = True
    $ remove_hook(label="house_block")
    $ remove_hook(label="home_afterwork")

    $ miniMapEnabledOnly = ["none"]
    $ add_hook("Teleport_Bedroom_MC", "ep05_dialogues4_college_emily_1a", scene="house_bedroom_mc_onbed", label="morning_block")
    call phone_instagram3b()
    $ add_hook("instagram", "ep15_quests1_emily_instagram", scene="phone")

    python:
        move_object("Sophie", "house_kitchen")
        move_object("Henry", "empty")
        move_object("Sister1", "house_sister1")
#        move_object("Sister2", "house_sister2")
        move_object("Friend_Bardie", "college_empty")
        sister1RoomDoorLocked = True
#        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True
        sophieCallStage = 0
        seanCallStage = 0

    return

label ep15_quests1_emily_instagram:
    if phone_instagram_current_name != "Emily":
        return
    $ remove_hook()
    $ phone_instagram_initial_position = 1.0
    call ep05_dialogues4_college_emily_2()
    $ questHelp("house_30", True)
    $ remove_hook(label="morning_block")
    $ add_hook("phone_close", "ep15_quests1_emily_instagram_close", scene="phone")

    return

label ep15_quests1_emily_instagram_close:
    $ remove_hook()
    $ phone_instagram_initial_position = 0.0
    $ house_bedroom_mc_onbed_suffix = 1
    $ miniMapEnabledOnly = []
    $ questHelp("college_32")

    call change_scene("house_bedroom_mc", "Fade_long")
    $ set_object_follow_way("college_coridor1", from_everywhere=True)
#    $ miniMapDisabled["COLLEGE"] = []
    $ autorun_to_object("ep05_dialogues4_college_emily_3", scene="college_street")

    $ add_hook("Teleport_Coridor1", "ep15_quests2_enter_college", scene="college_street", quest="day8")
    $ focus_map("Teleport_COLLEGE", "ep04_dialogues1_family_sophie_1b")

    sound2 put_dress
    call refresh_scene_fade_long()
    return

label ep15_quests2_enter_college:
    $ remove_hook()
    $ questHelp("college_32", True)
    call ep05_dialogues4_college_emily_4()

    $ unfocus_map()
    $ add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", label="college_block", quest="day8") #Мне пока там нечего делать.
    call changeDayTime("evening")

    call ep05_dialogues4_college_emily_5() # сцена с Шоном и Софи (запускается автоматически сразу после предыдущего лейбла)
    $ questHelpDesc("sean_desc3")
    $ questHelpDesc("college_desc14", False)

    $ remove_hook(quest="day8")

    call changeDayTime("morning")

    call ep05_dialogues4_college_emily_6()
    call ep05_dialogues1_college_sarah_1()

    $ seanCallStage = 7
    $ emilyCallStage = 6

    python:
        move_object("Sophie", "house_kitchen")
        move_object("Henry", "empty")
        move_object("Sister1", "house_sister1")
        move_object("Sister2", "house_sister2")
        move_object("Friend_Bardie", "college_empty")
        sister1RoomDoorLocked = True
        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True
        sophieCallStage = 0

    $ autorun_to_object("ep15_quests3_morning", scene="house_bedroom_mc_onbed")

    $ house_bedroom_mc_onbed_suffix = 2
    call change_scene("house_bedroom_mc_onbed", "Fade_long", False)
    return False

label ep15_quests3_morning:
    call ep05_dialogues1_college_sarah_1a()
    call process_change_map_location("HOUSE")
#    $ phone_focus_icon(True)
    $ set_object_follow_way("college_coridor1", from_everywhere=True)
    $ questHelp("college_33")
    $ questHelp("college_34")
    $ add_hook("Teleport_Coridor1", "ep15_quests4_college", scene="college_street", quest="day9")
    $ focus_map("Teleport_COLLEGE", "ep04_dialogues1_family_sophie_1b")
    $ add_hook("phone_close", "ep15_quests3_morning2", scene="phone", once=True, quest="day9")
    $ phone_incoming_call("Emily")
    $ remove_hook(label="house_block")
#    $ phone_incoming_call("Sean")

#    $ add_hook("enter_scene", "ep15_quests3_morning2_emily_call", scene="house_bedroom_mc", once=True, quest="day9")

    return

label ep15_quests3_morning2:
    pause 0.5
    call change_scene("house_bedroom_mc", "Fade_long", "put_dress")
    sound2 put_dress
    call refresh_scene_fade_long()
    return

#label ep15_quests3_morning2_emily_call:
#    $ house_bedroom_mc_onbed_suffix = 1
#    $ phone_incoming_call("Emily")
#    $ set_object_follow_way("college_coridor1", from_everywhere=True)

#    return

label ep15_quests4_college:
    $ remove_hook()
    $ questHelp("college_33", True)
    $ questHelp("college_34", True)
    call ep05_dialogues1_college_sarah_2() # клик на колледж, библиотека

    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor2", "COLLEGE_Floor3", "COLLEGE_Street"]

    $ add_hook("Teleport_English", "ep01_dialogues2_day1_family_1_12", scene="college_coridor6", label="block_english") # мне пока нечего там делать
    $ add_hook("Teleport_Algebra", "ep01_dialogues2_day1_family_1_12", scene="college_coridor5", label="block_algebra") # мне пока нечего там делать
    $ set_active("Teleport_Coridor5", True, scene="college_artclass")
    $ add_hook("Teleport_Library", "ep01_dialogues2_day1_family_1_12", scene="college_coridor9", label="block_library") # мне пока нечего там делать
    $ add_hook("Teleport_Principal_Secretary", "ep01_dialogues2_day1_family_1_12", scene="college_coridor8", label="block_principal_secretary") # мне пока нечего там делать
    $ add_hook("Teleport_Street", "ep05_dialogues1_college_sarah_1b", scene="college_coridor1", label="block_exit_college", quest="day9") #У меня остались еще дела здесь...
    $ questHelp("college_35")
    $ sarahAppearingDisabled = True
    $ set_object_follow_way("college_gym", from_everywhere=True)
    call college_gym_init2()
#    $ add_hook("Sarah", "ep15_quests4_college_sarah", scene="college_gym", quest="day9")
    $ add_hook("Teleport_Gym", "ep15_quests4_college_sarah", scene="college_coridor2", quest="day9")
    call change_scene("college_coridor2", "Fade_long")
    return False

label ep15_quests4_college_sarah:
    call ep05_dialogues1_college_sarah_3()
    $ questHelp("college_35", True)
    call changeDayTime("day")
    $ autorun_to_object("ep05_dialogues1_college_sarah_2a", scene="college_gym")
    $ set_object_follow_way("college_street", from_everywhere=True)
    $ move_object("Sarah", "empty")
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor1", "COLLEGE_Floor2", "COLLEGE_Floor3", "COLLEGE_Street"]
    $ add_hook("Teleport_Coridor2", "ep15_quests4_college_after", scene="college_gym", quest="day9")
    $ questHelpDesc("college_desc15")
    $ questHelpDesc("college_desc1", False)
    $ questHelpDesc("college_desc13", False)
    
#    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor1", "COLLEGE_Floor2", "COLLEGE_Floor3"]
    return

label ep15_quests4_college_after:
    $ add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", label="college_block", quest="day9") #Мне пока там нечего делать.
    $ miniMapDisabled["COLLEGE"] = ["COLLEGE_Floor1", "COLLEGE_Floor2", "COLLEGE_Floor3"]
    $ add_hook("enter_scene", "ep15_quests4_college_after_street", scene="college_street", quest="day9", once=True)
    call change_scene("college_street", "Fade_long")

    return False

label ep15_quests4_college_after_street:
    call ep05_dialogues1_college_sarah_2b()
    $ remove_hook(label="bikerent_work")
    $ add_hook("FatherFriend", "ep15_quests5_bikerent", scene="beach_park", label="bikerent_work")
    if questHelpGetStatus("work_7") == 0:
        $ questHelpRemove("work_7")
    $ questHelp("work_8")
    $ set_object_follow_way("beach_park", from_everywhere=True)
    $ unfocus_map()
    $ move_object("Sophie", "empty")
    $ add_hook("bike_rental_end_evening", "ep15_quests6_bikerent_after", scene="global", quest="day9")
#        move_object("Sophie", "house_kitchen")
#        move_object("Henry", "empty")
#        move_object("Sister1", "house_sister1")
#        move_object("Sister2", "house_sister2")
#        move_object("Friend_Bardie", "college_empty")

    return

label ep15_quests5_bikerent:
    if ep15_bike_rental_scene == 0:
        $ ep15_bike_rental_scene = day
        if ep14_bikerent_work_count < 3:
            $ ep04_dialogues8_work_bikerental_2_noevening_day = day
            call ep04_dialogues8_work_bikerental_2()
        call ep05_dialogues8_work_bikerental_1()
        $ ep14_bikerent_work_count += 1
        $ questHelp("work_8", True)

        $ ep14_bikerent_work_lastday = day
        call process_hooks("bike_rental_end", "global")
        if _return == False:
            return False
        call changeDayTime("evening")
        call refresh_scene_fade()
        call process_hooks("bike_rental_end_evening", "global")
        return False


    call ep04_dialogues8_work_bikerental_2()
    $ ep14_bikerent_work_count += 1
    call process_hooks("bike_rental_end", "global")
    if _return == False:
        return False
    call changeDayTime("evening")
    call refresh_scene_fade()
    call process_hooks("bike_rental_end_evening", "global")
    return False

    
label ep15_quests6_bikerent_after:
    $ remove_hook()
    $ clear_object_follow_all()
    if questHelpGetStatus("becky_1") == 0:
        $ set_object_follow_way("mall_street")

    $ set_object_follow_way("house_street", merge=True)

    $ add_hook("before_open", "ep15_quests7_bedroom_mc", scene="house_bedroom_mc", quest="day9", once=True)


    return

label ep15_quests7_bedroom_mc:
    call changeDayTime("night")
    $ add_hook("Bed", "ep15_quests7_bed", scene="house_bedroom_mc", quest="day9")
    return

label ep15_quests7_bed:
    sound put_dress
    fadeblack 1.0
    $ house_bedroom_mc_onbed_suffix = 2
    $ add_hook("enter_scene", "ep15_quests7_bed2", scene="house_bedroom_mc_onbed", quest="day9", once=True)
    call change_scene("house_bedroom_mc_onbed", "Fade_long", False)
    return False

label ep15_quests7_bed2:
    $ emilyCallStage = 0
    $ seanCallStage = 0
    $ sarahCallStage = 1
    $ phone_incoming_call("Sarah")
    $ add_hook("phone_close", "ep15_quests7_bed3", scene="phone", quest="day9", once=True)
    return

label ep15_quests7_bed3:
    pause 0.5
    $ sarahCallStage = 2
    $ add_hook("Sarah", "ep15_quests8_sarah_gym", scene="college_gym", label="sarah_gym_regular")
    call ep03_dialogues3_family_evening_4() #регулярный сон
    $ remove_hook(quest="day9")
    $ add_hook("change_day_time", "ep15_quests9_morning_daisy", scene="global", label="check_daisy_call2")
    $ clear_object_follow_all()

    $ houseLifeStageSub1 = 1
    call house_floor2_init2() # инитим сестер
    $ add_hook("Sister1", "ep15_quests10_sister1", scene="house_floor2", label="sisters1")
    $ add_hook("Sister2", "ep15_quests10_sister1", scene="house_floor2", label="sisters1")
    $ add_hook("Teleport_Sister1", "ep15_quests10_sister1", scene="house_floor2", label="sisters1")
    $ add_hook("Teleport_Sister2", "ep15_quests10_sister1", scene="house_floor2", label="sisters1")

    call changeDayTime("morning")
    fadeblack 1.5
    $ set_room_parent("house_bedroom_mc_onbed", "house_bedroom_mc")
    $ set_object_follow_way("house_floor2", merge=True)

    $ questHelp("house_31")

    # Суббота
    # блокируем колледж
    $ add_hook("Teleport_Coridor1", "ep01_dialogues2_day1_family_1_12", scene="college_street", label="college_block")

    # инитим регулярную кровать
    $ remove_hook(label="ep14_quests4_evening_bed")
    $ add_hook("Bed", "bed_sleep1", scene="house_bedroom_mc", label="bed_regular")
    $ add_hook("before_sleep_actions", "bed_sleep1_bedsleep1", scene="global", label="sleep_regular", priority=1)
    $ add_hook("before_sleep_actions", "ep03_dialogues3_family_evening_4", scene="global", label="before_sleep_regular")
    $ add_hook("sleep", "bed_sleep1_bedsleep2", scene="global", label="sleep_regular")
    $ add_hook("after_sleep", "ep15_quests11_sunday_morning", scene="global", label="sunday_morning", once=True)

#    call change_scene("house_bedroom_mc", False, False)
#    $ add_hook("enter_scene", "ep15_quests9_morning", scene="house_bedroom_mc_onbed")
#    call change_scene("house_bedroom_mc_onbed", "Fade_long", False)
    call refresh_scene_fade_long()
    return

label ep15_quests8_sarah_gym:
    call ep05_dialogues1_college_sarah_5()
    call refresh_scene_fade_long()
    return False


label ep15_quests9_bed_skip_evening: # ждать до вечера
    if day_time_idx >= 2:
        return
    call ep05_dialogues2_family_daisy_3b()
    if _return == 1:
        $ house_bedroom_mc_onbed_suffix = 1
        call changeDayTime("evening")
        call change_scene("house_bedroom_mc_onbed", "Fade_long", False)
    return False

label ep15_quests10_sister1: # сестры
    if get_active_objects("Sister2", scene="house_floor2") != False and get_active_objects("Sister1", scene="house_floor2") != False:
        $ remove_hook(label="sisters1")
        call ep05_dialogues5_family_olivia_1()
        $ questHelp("house_31", True)
        $ questHelp("house_32")

        $ add_hook("Teleport_Sister1", "ep15_quests10_sister2_Olivia", scene="house_floor2", label="sisters2")
        $ add_hook("Teleport_Sister2", "ep15_quests10_sister2_Cynthia", scene="house_floor2", label="sisters2")
        $ houseLifeStageSub1 = 2
        $ oliviaCallStage = 2
        $ move_object("Sister1", "house_sister1")
        $ move_object("Sister2", "house_sister2")
        $ add_hook("enter_scene", "ep15_quests10_sister1a", scene="house_bedroom_mc", label=["sisters2_phone", "sisters2"])
        $ add_hook("enter_scene", "ep15_quests10_sister1a", scene="house_street", label=["sisters2_phone", "sisters2"])
        $ set_object_follow_way("house_sister2")
        call refresh_scene_fade_long()
        return False
    return
label ep15_quests10_sister1a: # сестры
    $ remove_hook(label="sisters2_phone")
    $ phone_incoming_call("Olivia")
    return

label ep15_quests10_sister2_Olivia: #
    if get_active_objects("Sister1", scene="house_sister1") == False:
        return
    if day_time_idx >= 2:
        $ sister1RoomDoorLocked = True
        call ep12_quests6_gymclosed()
        return False
    call ep05_dialogues5_family_olivia_2()
    call refresh_scene_fade()
    return False

label ep15_quests10_sister2_Cynthia: #
    if get_active_objects("Sister2", scene="house_sister2") == False:
        return
    if day_time_idx >= 2:
        $ sister2RoomDoorLocked = True
        call ep12_quests6_gymclosed()
        return False
    $ remove_hook(label="sisters2")
    call ep05_dialogues6_family_cynthia_1()
    $ questHelp("house_32", True)
    $ floor2Sister1Suffix = 1
    $ houseLifeStageSub1 = 3
    $ oliviaCallStage = 3
    $ cynthiaCallStage = 5
    $ sister1RoomDoorLocked = True
    $ add_hook("Sister1", "ep15_quests10_sister3_Olivia", scene="house_floor2", label="sisters3")
    $ questHelp("house_33")
    $ move_object("Sister1", "house_floor2")
    $ clear_object_follow_all()
    call refresh_scene_fade()
    return False

label ep15_quests10_sister3_Olivia: #
    $ remove_hook(label="sisters3")
    call ep05_dialogues5_family_olivia_3()
    $ questHelp("house_33", True)
    $ move_object("Sister1", "house_sister1")
    if questHelpGetStatus("work_9") == 0:
        $ set_object_follow_way("daisy_street", from_everywhere = True)

    $ ep15_quests10_sister3_Olivia_day = day
    $ add_hook("enter_scene", "ep15_quests10_sister3_Olivia_phone", scene="house_bedroom_mc", label=["sisters3_phone"])
    $ add_hook("enter_scene", "ep15_quests10_sister3_Olivia_phone", scene="house_street", label=["sisters3_phone"])
    $ oliviaCallStage = 4
    $ cynthiaCallStage = 5
    $ houseLifeStageSub1 = 0
    $ questHelpDesc("house_desc12")
    $ questHelpDesc("house_desc7", False)
    $ questHelpDesc("house_desc9", False)

    call refresh_scene_fade()
    return False

label ep15_quests10_sister3_Olivia_phone: #
    if ep15_quests10_sister3_Olivia_day == day:
        return
    if ep15_quests10_sister3_Olivia_phone_day == day:
        return
    $ ep15_quests10_sister3_Olivia_phone_day = day
    if phone_check_chat("olivia_chat4") == False:
        $ phone_incoming_call("Olivia")
        return
    if phone_check_chat("cynthia_chat5") == False:
        $ phone_incoming_call("Cynthia")
    $ remove_hook(label="sisters3_phone")
    return

label ep15_quests11_sunday_morning: # утро воскресения
    $ autorun_to_object("ep05_dialogues3_work_daisy_1", scene="house_bedroom_mc_onbed")
    $ miniMapHouseGenerate_mode = 1
    $ add_hook("before_sleep_actions", "ep15_quests13_sleep", scene="global", label="ep15_end")
    $ remove_hook(label="house_block")
    call ep15_quests12_init_sophie()
    music Little_Tomcat
    call refresh_scene_fade_long()
    return


label ep15_quests12_init_sophie: # проверка на Софи
    if ep15_quests12_init_sophie_flag == True:
        return
    $ print "init sophie!!!"
    if mlsBardiFamilyV4Sophie2 == 0 or mlsBardiFamilyV4Sophie3 == 0:
        return
    $ ep15_quests12_init_sophie_flag = True
    $ add_hook("before_open", "ep15_quests12_sophie1", scene="house_floor1", label="sophie_evening1")
    $ add_hook("before_open", "ep15_quests12_sophie2_kitchen", scene="house_kitchen", label="sophie_evening1")
    $ add_hook("Bed", "ep05_dialogues7_family_sophie_1a", scene="house_bedroom_mc", label="sophie_evening1")
    $ questHelp("house_34")
    return

label ep15_quests12_sophie1: # before_open
    if day_time_idx >= 2:
        $ move_object("Sophie", "house_kitchen")
        $ landLordRoomDoorLocked = False
    return


label ep15_quests12_sophie2_kitchen: #
    if day_time_idx >= 2:
        $ remove_hook(label="sophie_evening1")
        call ep05_dialogues7_family_sophie_1()
        call changeDayTime("night")
        $ landLordRoomDoorLocked = False
        $ questHelp("house_34", True)
        call house_bedroom_landlord_init()
        $ move_object("Henry", "empty")
        $ move_object("Sophie", "house_bedroom_landlord")
        $ add_hook("Sophie", "ep15_quests12_sophie3_sleep", scene="house_bedroom_landlord", label="evening_time_temp")
        $ houseBedroomLandlordSophieSuffix = "Sleep1"
        call change_scene("house_floor2", "Fade_long")
        call refresh_scene_fade_long()
        return False
    return

label ep15_quests12_sophie3_sleep: #
    call ep05_dialogues7_family_sophie_1b()
    call refresh_scene_fade()
    return

label ep15_quests13_sleep:
    $ houseBedroomLandlordSophieSuffix = 1
    jump end_update
    return


