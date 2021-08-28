default ep219_quests_escort1_init_flag = 0
default ep219_quests_escort2_biff_day = 0
default ep219_quests_linda_angry_blocked = 0
default lindaApartmentsStage = 0
default ep219_quests_linda_visit_day = 0
default ep219_quests_linda_after_stage = 0
default ep219_quests_linda_after_stage_day = 0

label ep219_quests_escort1_init:
    if ep219_quests_escort1_init_flag > 0:
        return
    if ep217_quests_presentation_completed2_day == 0:
        return
    if monica_escort_service_started == True and ep212_escort_monica_fired == False and ep212_escort3_monica_fired == False and ep212_escort5_monica_fired == False and ep217_party_day == 0:
        return # есть эскорт, но квест не пройден
    $ ep219_quests_escort1_init_flag = day
    $ add_talk("Biff", "ep219_quests_escort2_biff", scene="monica_office_cabinet_table", label="ep219_quests_escort2_biff")
    $ questHelp("office_59")
    return


label ep219_quests_escort2_biff: # разговор у Бифа, приходит Линда
    if day == ep217_quests_presentation_completed2_day:
        return
    call ep219_dialogues3_escort_1() from _rcall_ep219_dialogues3_escort_1
    if _return == False:
        $ questHelp("office_59", False)
        call putoff_work_clothes() from _rcall_putoff_work_clothes_16 # уходим из офиса
        call change_scene("street_monica_office", "Fade_long") from _rcall_change_scene_237
        return False


    $ questHelp("office_59", True)
    if monica_escort_service_started == True and ep212_escort_monica_fired == False and ep212_escort3_monica_fired == False and ep212_escort5_monica_fired == False:
        $ questHelp("escort_24")
        $ add_hook("before_open", "ep219_quests_escort3_linda", scene="rich_hotel_reception", label="ep219_quests_escort3_linda")
    call ep219_quests_photoshoot1_init() from _rcall_ep219_quests_photoshoot1_init
    $ remove_hook(label="ep219_quests_escort2_biff")
    $ ep219_quests_escort2_biff_day = day
    $ ep219_quests_linda_angry_blocked = day
    call change_scene("monica_office_secretary", "Fade_long") from _rcall_change_scene_238

    return False

label ep219_quests_escort3_linda: # Линда встречает Монику в отеле
    if cloth != "CasualDress1":
        return
    $ remove_hook()
    call ep219_dialogues3_escort_2() from _rcall_ep219_dialogues3_escort_2
    $ questHelp("escort_24", True)
    $ questHelp("escort_25")
    $ add_hook("before_open", "ep219_quests_escort4_choose", scene="street_rich_hotel", label="ep219_quests_escort4_choose")
    return

label ep219_quests_escort4_choose: # выбор идти-ли к Линде
    $ remove_hook()
    $ map_objects ["Teleport_LindaHome"] = {"text" : t_("АПАРТАМЕНТЫ ЛИНДЫ"), "xpos" : 1680, "ypos" : 437, "base" : "map_marker", "state" : "visible"}
    $ lindaApartmentsStage = 0
    $ add_hook("map_teleport", "ep219_quests_escort5_lindahome", scene="global", label="escort_linda_teleport")
    $ add_hook("Visitor2", "ep219_quests_escort4_lindarepeat", scene="rich_hotel_restaurant", label="ep219_quests_escort4_lindarepeat")
#    call locations_init_linda_apartments()
#    $ add_hook("before_open", "ep219_quests_escort5_lindahome", scene="linda_apartments_street", label="ep219_quests_escort5_lindahome")
    call ep219_dialogues3_escort_3() from _rcall_ep219_dialogues3_escort_3
    if _return == True:
        $ map_enabled = True
        $ sceneIsStreet = True
        call map_show() from _rcall_map_show_3
    else:
        $ map_enabled = True
        $ questHelp("escort_25", False)
        call refresh_scene_fade()
    return

label ep219_quests_escort4_lindarepeat:
    call ep219_dialogues3_escort_3a() from _rcall_ep219_dialogues3_escort_3a
    return False

label ep219_quests_escort5_lindahome:
    if obj_name != "Teleport_LindaHome":
        return
    if lindaApartmentsStage == 0:
        if day_time != "evening":
            $ changeDayTime("evening")
        $ remove_hook(label="ep219_quests_escort4_lindarepeat")
        call ep219_dialogues3_escort_4() from _rcall_ep219_dialogues3_escort_4
        call ep219_dialogues3_escort_5() from _rcall_ep219_dialogues3_escort_5
        $ add_hook("before_open", "ep219_quests_escort6_hotel_after", scene="rich_hotel_reception", label="ep219_quests_escort6_linda_hotel")
        $ ep219_quests_linda_visit_day = day
        $ lindaApartmentsStage = 1
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep215_dialogues3_escort_24_block", scene="street_rich_hotel", label="evening_time_temp")
        $ autorun_to_object("ep219_dialogues3_escort_8", scene="street_house_outside")
        $ questHelp("escort_25", True)
        $ questHelp("escort_26")
        fadeblack 2.0
        call process_change_map_location("House") from _rcall_process_change_map_location_12
        $ map_source_scene = "street_house_outside"
#        call change_scene("street_house_outside", "Fade_long")
        return False
    if lindaApartmentsStage == 1:
        call ep25_dialogues1_shop3() from _rcall_ep25_dialogues1_shop3
        return False
    return False

label ep219_quests_escort6_hotel_after: # встреча с Линдой при входе в отель (после)
    if cloth != "CasualDress1":
        return
    if ep219_quests_linda_after_stage == 0:
        call ep219_dialogues3_escort_6() from _rcall_ep219_dialogues3_escort_6
        $ ep219_quests_linda_after_stage = 1
        $ ep219_quests_linda_after_stage_day = day
        $ questHelp("escort_26", True)
        $ questHelp("escort_27")
        return

    if ep219_quests_linda_after_stage == 1 and ep219_quests_linda_after_stage_day != day:
        call ep219_dialogues3_escort_7() from _rcall_ep219_dialogues3_escort_7
        $ ep219_quests_linda_after_stage = 2
        $ ep219_quests_linda_after_stage_day = day
        $ questHelp("escort_27", True)
        call ep224_quests_escort_init() from _rcall_ep224_quests_escort_init_2
        return
    return


#
