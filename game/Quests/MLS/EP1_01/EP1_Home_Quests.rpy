label ep1_home_quests1_init:
    $ questHelp("house_5")
    $ set_object_follow("Teleport_Floor1", scene="house_street")
    $ set_object_follow("Teleport_Kitchen", scene="house_floor1")
    $ set_object_follow("Teleport_Floor1", scene="house_floor2")
    $ set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
    $ set_object_follow("House_Bedroom_MC", scene="minimap")

    # проверяем на время дня, меняем на вечер, блокируем выход и расставляем персонажей
    $ add_hook("exit_scene", "ep1_home_quests2_check_evening", scene="house_street", quest="day1", label="check_evening")
    return

label ep1_home_quests2_check_evening:
    if target_scene_name == "house_floor1" or check_scene_parent(target_scene_name, "house_floor1", recursive=True) != False:
        $ remove_hook()
        # блокируем выход из дома
        $ add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block")
        $ miniMapDisabled["HOUSE"] = ["House_Street"]

        if day_time_idx < 2:
            call changeDayTime("evening") from _rcall_changeDayTime_6
            fadeblack 2.0

        $ move_object("Sister1", "house_sister1")
        $ move_object("Sister2", "house_sister2")
        $ move_object("Sophie", "house_kitchen")
        $ move_object("Henry", "house_kitchen")

        $ sister1RoomDoorLocked = True
        $ sister2RoomDoorLocked = True
        $ landLordRoomDoorLocked = True

        $ add_hook("before_open", "ep1_home_quests3_kitchen", scene="house_kitchen")

    return

label ep1_home_quests3_kitchen: # разговор на кухне
    $ remove_hook()
    $ clear_object_follow_all()
    call ep01_dialogues3_day2_family_6() from _rcall_ep01_dialogues3_day2_family_6
    $ miniMapDisabled["HOUSE"] = ["House_Street"]
    $ add_hook("before_open", "ep1_home_quests4_sister1", scene="house_floor2", quest="day1", label="meet_sister1")
    $ add_hook("before_open", "ep1_home_quests4_sister1", scene="house_bedroom_mc", quest="day1", label="meet_sister1")
    $ add_hook("Bed", "ep1_home_quests5_bed", scene="house_bedroom_mc", quest="day1", label="bed")
    $ add_hook("Sophie", "ep1_home_quests4_sophie", scene="house_kitchen", quest="day1")
    $ questHelp("house_5b")
    $ move_object("Henry", "housefriend_bedroom_parents")
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_5
    return False

label ep1_home_quests4_sister1: # встреча с сестрой на 2-ом этаже
    $ remove_hook(label="meet_sister1")
    call ep01_dialogues3_day2_family_6a3() from _rcall_ep01_dialogues3_day2_family_6a3
    $ add_hook("Teleport_Sister1", "ep01_dialogues3_day2_family_6a", scene="house_floor2", quest="day1", label="block_sister1")
    $ add_hook("Teleport_Sister2", "ep01_dialogues3_day2_family_6b", scene="house_floor2", quest="day1", label="block_sister2")
    $ questHelp("house_6")
    $ questHelpDesc("house_desc6")
    $ add_hook("Bed", "ep01_dialogues3_day2_family_6a2", scene="house_bedroom_mc", quest="day1", label="bed_block_instagram")
    call phone_instagram1_Olivia() from _rcall_phone_instagram1_Olivia
    $ add_hook("instagram", "ep1_home_quests6_instagram", scene="phone", label="ep1_home_quests4_sophie", once=True)
    call change_scene("house_bedroom_mc", "Fade_long", False) from _rcall_change_scene_16
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_6
    return False

label ep1_home_quests4_sophie: # разговор на кухне с Софи
    call ep01_dialogues2_day1_family_4_1() from _rcall_ep01_dialogues2_day1_family_4_1
    call refresh_scene_fade() from _rcall_refresh_scene_fade_1
    return False

label ep1_home_quests5_bed: # ложится спать
    call ep01_dialogues2_day1_family_3() from _rcall_ep01_dialogues2_day1_family_3
    if _return == False:
        return False
    $ questHelp("house_5b", True)
    call changeDayTime("night") from _rcall_changeDayTime_7
    $ remove_hook(label="day1_college")
    $ remove_hook(quest="day1")
    call ep01_dialogues3_day2_family_7() from _rcall_ep01_dialogues3_day2_family_7
    $ steam_achievement("ach_end1")
    call ep12_quests1_init() from _rcall_ep12_quests1_init
    return False

#    jump end_update

label ep1_home_quests6_instagram:
    $ questHelp("house_6", True)
    $ questHelp("house_7")
    $ questHelp("house_8")
    $ questLog(2, True)
    $ remove_hook(label="bed_block_instagram")
    call ep01_dialogues3_day2_family_8a() from _rcall_ep01_dialogues3_day2_family_8a
    $ add_hook("phone_close", "ep01_dialogues3_day2_family_8b", scene="phone", label="ep01_dialogues3_day2_family_8b", once=True)
    return


#
