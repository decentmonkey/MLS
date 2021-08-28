default ep224_quests_escort_init_flag = False
default ep224_quests_meeting_planned = False
default ep224_quests_meeting2_planned = False
default ep224_quests_meeting2_day = 0
default ep224_quests_monica_kicked_client = 0
label ep224_quests_escort_init:
    if ep218_quests_meeting2_day == 0 or ep219_quests_linda_after_stage_day == 0:
        return
    if ep224_quests_escort_init_flag == True:
        return
    $ questHelp("escort_28")
    $ add_hook("Visitor4", "ep224_quests_escort1_abbyb", scene="rich_hotel_restaurant", label="ep224_quests_escort1_abbyb")
    $ ep224_quests_escort_init_flag = True
    $ ep224_quests_meeting_planned = True
    return

label ep224_quests_escort1_abby:
    $ remove_hook(label="ep224_quests_escort1_abbyb")
    $ ep224_quests_meeting_planned = False
    call ep22_4_dialogues5_escort_1() from _rcall_ep22_4_dialogues5_escort_1
    if _return == False:
        $ add_hook("Visitor4", "ep224_quests_escort2_abby_repeat", scene="rich_hotel_restaurant", label="ep224_quests_escort2_abby_repeat")
        return True
    jump ep224_quests_escort3_start

label ep224_quests_escort1_abbyb:
    $ remove_hook()
    $ ep224_quests_meeting_planned = False
    call ep22_4_dialogues5_escort_1() from _rcall_ep22_4_dialogues5_escort_1_1
    if _return == False:
        $ add_hook("Visitor4", "ep224_quests_escort2_abby_repeat", scene="rich_hotel_restaurant", label="ep224_quests_escort2_abby_repeat")
        return False
    jump ep224_quests_escort3_start

label ep224_quests_escort2_abby_repeat:
    call ep22_4_dialogues5_escort_2() from _rcall_ep22_4_dialogues5_escort_2
    if _return == False:
        return False
    jump ep224_quests_escort3_start

label ep224_quests_escort3_start:
    $ remove_hook(label="ep224_quests_escort2_abby_repeat")
    $ questHelp("escort_28", True)
    $ questHelp("escort_29")
    $ candiseApartmentsStage = 3
    call locations_init_candiseabby() from _rcall_locations_init_candiseabby
    $ autorun_to_object("ep22_4_dialogues5_escort_3", scene="street_candise")
    $ add_hook("Teleport_Inside", "ep224_quests_escort4_abby_apartments", scene="street_candise", label="ep224_quests_escort4_abby_apartments")
#    $ remove_hook(label="ep224_quests_escort2_abby_repeat")
    call change_scene("rich_hotel_reception", "Fade_long") from _rcall_change_scene_248
    return False

label ep224_quests_escort4_abby_apartments:
    if cloth != "CasualDress1":
        call ep22_4_dialogues5_escort_7a() from _rcall_ep22_4_dialogues5_escort_7a
        return False
    $ remove_hook(label="ep224_quests_escort4_abby_apartments")
    if day_time != "evening":
        $ changeDayTime("evening")
#    $ add_hook("Teleport_Rich_Hotel_Reception", "ep210_dialogues7_escort_hotel_7c1", scene="street_rich_hotel", label=["hotel_restrict_today", "evening_time_temp"]) # Блокируем отель на сегодня
    call ep22_4_dialogues5_escort_4() from _rcall_ep22_4_dialogues5_escort_4
    if _return == False:
        # выгнала
        $ autorun_to_object("ep22_4_dialogues5_escort_6", scene="street_candise")
        $ add_hook("Visitor4", "ep224_quests_escort2_abby_repeat", scene="rich_hotel_restaurant", label="ep224_quests_escort2_abby_repeat")
        $ questHelp("escort_29", False)
        $ ep224_quests_monica_kicked_client = day
    else:
        if monicaAbbyNoEscortClient4 > 0:
            $ autorun_to_object("ep22_4_dialogues5_escort_5", scene="street_candise")
        else:
            $ autorun_to_object("ep22_4_dialogues5_escort_5a", scene="street_candise")
        $ ep224_quests_monica_kicked_client = 0
        $ questHelp("escort_29", True)
    $ ep224_quests_meeting2_planned = True
    $ questHelp("escort_30")
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_31
    return False

label ep224_quests_escort5_abby_meeting:
    $ ep224_quests_meeting2_planned = False
    $ ep224_quests_meeting2_day = day
    call ep22_4_dialogues5_escort_8() from _rcall_ep22_4_dialogues5_escort_8
    if ep224_quests_monica_kicked_client > 0:
        $ questHelp("escort_30", False)
    else:
        $ questHelp("escort_30", True)
        call ep225_quests_escort1_1_init()
    return











#
