default ep15_update_init_flag = False

default ep15_bike_rental_scene = 0

label ep15_update_init:
    if ep15_update_init_flag == True:
        return
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
        return False


    call ep04_dialogues8_work_bikerental_2()
    $ ep14_bikerent_work_count += 1
    call process_hooks("bike_rental_end", "global")
    if _return == False:
        return False
    call changeDayTime("evening")
    call refresh_scene_fade()
    return False

    