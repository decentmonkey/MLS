default introHUDBlocked = False
default introKitchen1Day = 0
default ep1_intro_quests5_sophie_Flag = False
default ep1_intro_quests6_cynthia_bathroom_Flag = False
default mcShowerLastDay = 0
default sophieKitchenTalkLastDay = 0

label ep1_intro_quests1:
    call ep01_dialogues1_start_1a() from _rcall_ep01_dialogues1_start_1a # пляж, показываем геймплей
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_7
    $ introHUDBlocked = True
#    $ questHelp("start_1")
    return

label ep1_intro_quests1_block:
    hide screen hud_block
    call ep01_dialogues1_start_1a5() from _rcall_ep01_dialogues1_start_1a5
    call refresh_scene_fade() from _rcall_refresh_scene_fade_2
    return

label ep1_intro_quests2:
    hide screen hud_block
    $ introHUDBlocked = False
    call ep01_dialogues1_start_1a2() from _rcall_ep01_dialogues1_start_1a2
    hide screen hud_screen
    $ add_hook("enter_scene", "ep1_intro_quests3", scene="map")
    call map_show() from _rcall_map_show
    return

label ep1_intro_quests3:
    $ remove_hook()
    show screen sprites_hover_dummy_screen()
    call ep01_dialogues1_start_1ab3() from _rcall_ep01_dialogues1_start_1ab3
    $ questHelp("start_1", True)
#    call ep01_dialogues1_start_1b() from _rcall_ep01_dialogues1_start_1b # подглядывание за Оливией и Марком
    call ep01_dialogues1_start_2() from _rcall_ep01_dialogues1_start_2 # поезд
    call ep01_dialogues1_start_3() from _rcall_ep01_dialogues1_start_3 # вокзал

    call changeDayTime("evening") from _rcall_changeDayTime_8
    call phone_contacts1() from _rcall_phone_contacts1_2
    call ep01_dialogues2_day1_family_1() from _rcall_ep01_dialogues2_day1_family_1 # комната Барди перед ужином

    $ camera_icon_enabled = True

    python:
        questHelp("house_1")

        add_hook("Bed", "ep01_dialogues2_day1_family_1_1", scene="house_bedroom_mc", label="bed_block")
        autorun_to_object("ep01_dialogues2_day1_family_1_11", scene="house_livingroomhall")

        # комментарий про кухню (на следующий день)
        introKitchen1Day = day
        add_hook("enter_scene", "ep01_dialogues2_day1_family_1_15", scene="house_kitchen", label="ep01_dialogues2_day1_family_1_15")

        # закрываем двери
        sister1RoomDoorLocked = True
        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True

        # блокируем выход из дома
        add_hook("Teleport_Street", "ep01_dialogues2_day1_family_1_12", scene="house_floor1", label="house_block")
        miniMapDisabled["HOUSE"] = ["House_Street"]

        add_hook("before_open", "ep1_intro_quests4", scene="house_kitchen", label="ep1_intro_quests4")

        # душ
        add_hook("before_open", "ep1_intro_quests3_shower1", scene="house_bathroom", label="ep1_intro_quests3_shower1", once=True)
        add_hook("Shower", "ep1_intro_quests3_shower2", scene="house_bathroom", label="house_shower")
        add_hook("Toilet", "ep01_dialogues2_day1_family_1_13", scene="house_bathroom", label="house_toilet")
        add_hook("Bath", "ep01_dialogues2_day1_family_1_13a", scene="house_bathroom", label="house_bath")

        # собираем всех на кухню
        move_object("Sophie", "house_kitchen")
        move_object("Sister1", "house_kitchen")
        move_object("Sister2", "house_kitchen")
        move_object("Henry", "house_kitchen")

        # делаем ведение по указателям
        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Floor1", scene="house_floor2")
        set_object_follow("Teleport_Kitchen", scene="house_floor1")
        set_object_follow("Floor1", scene="minimap")

        autorun_to_object("ep01_dialogues2_day1_family_1_3", scene="house_bedroom_mc_tablenear")


    if _return == True:
        call change_scene("house_kitchen", "Fade_long") from _rcall_change_scene_17
        return
    call change_scene("house_bedroom_mc", "Fade_long") from _rcall_change_scene_18
    return

label ep1_intro_quests3_shower1:
    sound snd_door_open1
    call ep01_dialogues2_day1_family_1_14() from _rcall_ep01_dialogues2_day1_family_1_14
    call refresh_scene_fade() from _rcall_refresh_scene_fade_3
    return False
label ep1_intro_quests3_shower2:
    call ep01_dialogues2_day1_family_1_14b() from _rcall_ep01_dialogues2_day1_family_1_14b
    call refresh_scene_fade() from _rcall_refresh_scene_fade_4
    return False

label ep1_intro_quests4: # кухня
    call ep01_dialogues2_day1_family_2() from _rcall_ep01_dialogues2_day1_family_2 # кухня, ужин с семьей

    $ remove_hook(label="ep1_intro_quests4")

    $ clear_object_follow_all()

    $ questHelp("house_1", True)
    $ questHelpDesc("house_desc1")
    $ questHelp("house_2")
    $ autorun_to_object("ep01_dialogues2_day1_family_1_2", scene="house_bedroom_mc")

    $ sister1RoomDoorLocked = False
    $ sister2RoomDoorLocked = False
    $ landLordRoomDoorLocked = True

    $ move_object("Sophie", "house_kitchen")
    $ move_object("Sister1", "house_sister1")
    $ move_object("Sister2", "house_sister2")
    $ move_object("Henry", "house_livingroomhall")

    $ add_hook("Sophie", "ep1_intro_quests5_sophie", scene="house_kitchen", label="talk_evening")
    $ houseLivingRoomFatherSuffix = 3
    $ add_hook("Henry", "ep1_intro_quests5_henry", scene="house_livingroomhall", label="talk_evening")
    $ add_hook("before_open", "ep1_intro_quests5_henry", scene="house_livingroomhall", label=["henry_talk_livingroom_auto", "talk_evening"], once=True)
    $ add_hook("Teleport_Sister1", "ep01_dialogues2_day1_family_6", scene="house_floor2", label="talk_evening")
    $ add_hook("Teleport_Sister2", "ep01_dialogues2_day1_family_7", scene="house_floor2", label="talk_evening")
    $ add_hook("Bed", "ep1_intro_quests5_bed", scene="house_bedroom_mc", label="ep1_intro_quests5_bed")

    # делаем ведение по указателям
    $ set_object_follow("Teleport_Floor1", scene="house_kitchen")
    $ set_object_follow("Teleport_Floor2", scene="house_floor1")
    $ set_object_follow("Teleport_Bedroom_MC", scene="house_floor2")
    $ set_object_follow("House_Bedroom_MC", scene="minimap")

    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_8
    return

label ep1_intro_quests5_sophie: # разговор вечером
    if ep1_intro_quests5_sophie_Flag == False:
        call ep01_dialogues2_day1_family_4() from _rcall_ep01_dialogues2_day1_family_4
        $ ep1_intro_quests5_sophie_Flag = True
        call refresh_scene_fade() from _rcall_refresh_scene_fade_5
        return False
    call ep01_dialogues2_day1_family_4_1() from _rcall_ep01_dialogues2_day1_family_4_1_1
    call refresh_scene_fade() from _rcall_refresh_scene_fade_6
    return False

label ep1_intro_quests5_henry: # разговор вечером
    if get_active_objects("Henry", scene="house_livingroomhall") == False:
        return
    call ep01_dialogues2_day1_family_5() from _rcall_ep01_dialogues2_day1_family_5
    call refresh_scene_fade() from _rcall_refresh_scene_fade_7
    return False

label ep1_intro_quests5_bed: # ложится спать
    call ep01_dialogues2_day1_family_3() from _rcall_ep01_dialogues2_day1_family_3_1
    if _return == False:
        return False
    $ remove_hook(label="ep1_intro_quests5_bed")
    $ clear_object_follow_all()
    $ questHelp("house_2", True)
    call ep01_dialogues2_day1_family_8() from _rcall_ep01_dialogues2_day1_family_8
    if steamVersion == False:
        $ questHelp("house_3")
    $ questHelp("house_4")
    call changeDayTime("morning") from _rcall_changeDayTime_9
    $ remove_hook(label="talk_evening")
    call ep01_dialogues3_day2_family_1() from _rcall_ep01_dialogues3_day2_family_1

    python:
        move_object("Sister2", "house_bathroom")
        move_object("Sister1", "house_sister1")
        move_object("Henry", "empty")
        move_object("Sophie", "house_kitchen")

        sister1RoomDoorLocked = True
        sister2RoomDoorLocked = True
        landLordRoomDoorLocked = True

        if steamVersion == True:
            move_object("Sister2", "house_sister2")
        else:
            add_hook("Teleport_Bathroom", "ep1_intro_quests6_cynthia_bathroom", scene="house_floor1", label="day1_morning")
        add_hook("Sophie", "ep1_intro_quests6_sophie2", scene="house_kitchen", label="sophie_morning_regular")
        add_hook("Sophie", "ep1_intro_quests6_sophie", scene="house_kitchen", label="day1_morning")

        set_object_follow("Teleport_Floor2", scene="house_bedroom_mc")
        set_object_follow("Teleport_Floor1", scene="house_floor2")
        set_object_follow("Teleport_Kitchen", scene="house_floor1")
        set_object_follow("Floor1", scene="minimap")

    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_9
    return False

label ep1_intro_quests6_cynthia_bathroom: # душ Синтия
    if get_active_objects("Sister2", scene="house_bathroom") == False:
        return
    if ep1_intro_quests6_cynthia_bathroom_Flag == False:
        call ep01_dialogues3_day2_family_2() from _rcall_ep01_dialogues3_day2_family_2
        if _return == -1:
            $ questHelp("college_4", False)
        else:
            $ questHelp("college_4")

        $ ep1_intro_quests6_cynthia_bathroom_Flag = True
        $ questHelp("house_3", True)
        $ questHelpDesc("house_desc1", "house_desc2")
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_10
        return False
    call ep01_dialogues3_day2_family_3() from _rcall_ep01_dialogues3_day2_family_3
    return False

label ep1_intro_quests6_sophie: # Софи с утра на кухне
    if sophieKitchenTalkLastDay < day:
        call ep01_dialogues3_day2_family_4() from _rcall_ep01_dialogues3_day2_family_4
        $ questHelp("house_4", True)
        $ questHelp("college_1")
        $ questHelpDesc("college_desc1")
        $ remove_hook(label="house_block")
        $ miniMapDisabled = {}
        $ map_objects["Teleport_COLLEGE"] = {"text" : t_("КОЛЛЕДЖ"), "xpos" : 982, "ypos" : 268, "base" : "map_marker", "state" : "visible"}
        $ set_object_follow("Teleport_Coridor1", scene="college_street")
        $ add_hook("Teleport_Coridor1", "ep1_college_sean", scene="college_street", label="college_sean")
        $ add_hook("Friend_Bardie", "ep1_college_sean", scene="college_street", label="college_sean")
        $ clear_object_follow_all()
        $ sophieKitchenTalkLastDay = day
        $ autorun_to_object("ep01_dialogues3_day2_family_4a", scene="house_street")

        $ add_hook("before_open", "ep1_college_open", scene="college_street", once=True)

        $ clear_object_follow_all()
        $ set_object_follow("Teleport_Floor1", scene="house_kitchen")
        $ set_object_follow("Teleport_Street", scene="house_floor1")
        $ set_object_follow("Teleport_Map", scene="house_street")
        $ set_object_follow("House_Street", scene="minimap")
        $ set_object_follow("Teleport_COLLEGE", scene="map")

        call refresh_scene_fade() from _rcall_refresh_scene_fade_8
        return False
    call ep01_dialogues3_day2_family_5() from _rcall_ep01_dialogues3_day2_family_5
    return False

label ep1_intro_quests6_sophie2: # Софи утром регулярно
    if day_time_idx == 0:
        call ep01_dialogues3_day2_family_5() from _rcall_ep01_dialogues3_day2_family_5_1
        call refresh_scene_fade() from _rcall_refresh_scene_fade_9
        return False
    return

# Без душа fail college_4, house_3
#
