default ep217_quests_philip_visited_day = 0
default ep217_quests_philip_refused = 0

label ep217_quests_philip1: # едут к Филиппу
    $ ep217_quests_philip_visited_day = day
    $ questHelp("philip_8", True)
    call ep217_dialogues5_phillip_1() from _rcall_ep217_dialogues5_phillip_1
    if _return == False: # убежала не спустившись в подвал
        call process_change_map_location("PhilipHome") from _rcall_process_change_map_location_6
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep210_dialogues7_escort_hotel_7c1", scene="street_rich_hotel", label=["hotel_restrict_today", "evening_time_temp"]) # Блокируем отель на сегодня
        $ add_hook("escort_start_day", "ep217_quests_philip2_escort", scene="global", label="philip_anal1_escort")
        if monica_escort_service_started == True and ep212_escort_monica_fired == False and ep212_escort3_monica_fired == False and ep212_escort5_monica_fired == False:
            $ questHelp("escort_18")
        $ ep217_quests_philip_refused = 1
        $ questHelp("philip_10", False)
        $ autorun_to_object("ep217_dialogues5_phillip_6", scene="street_philiphome")
        $ add_hook("Teleport_Building", "ep217_dialogues5_phillip_6", scene="street_philiphome", label=["private_presentation1_philip_block_after", "evening_time_temp"])
        call change_scene("street_philiphome", "Fade_long") from _rcall_change_scene_213
        return False


    call ep217_dialogues5_phillip_2() from _rcall_ep217_dialogues5_phillip_2 #БДСМ комната
    if _return == False: # убежала из комнаты
        call process_change_map_location("PhilipHome") from _rcall_process_change_map_location_7
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep210_dialogues7_escort_hotel_7c1", scene="street_rich_hotel", label=["hotel_restrict_today", "evening_time_temp"]) # Блокируем отель на сегодня
        $ add_hook("escort_start_day", "ep217_quests_philip2_escort", scene="global", label="philip_anal1_escort")
        if monica_escort_service_started == True and ep212_escort_monica_fired == False and ep212_escort3_monica_fired == False and ep212_escort5_monica_fired == False:
            $ questHelp("escort_18")
        $ ep217_quests_philip_refused = 2
        $ questHelp("philip_10", False)
        $ autorun_to_object("ep217_dialogues5_phillip_6", scene="street_philiphome")
        $ add_hook("Teleport_Building", "ep217_dialogues5_phillip_6", scene="street_philiphome", label=["private_presentation1_philip_block_after", "evening_time_temp"])
        call change_scene("street_philiphome", "Fade_long") from _rcall_change_scene_214
        return False

    # сцена завершена успешно

    call process_change_map_location("PhilipHome") from _rcall_process_change_map_location_8
    $ add_hook("Teleport_Rich_Hotel_Reception", "ep210_dialogues7_escort_hotel_7c1", scene="street_rich_hotel", label=["hotel_restrict_today", "evening_time_temp"]) # Блокируем отель на сегодня
    if monica_escort_service_started == True and ep212_escort_monica_fired == False and ep212_escort3_monica_fired == False and ep212_escort5_monica_fired == False:
        $ questHelp("escort_18")

    $ add_hook("escort_start_day", "ep217_quests_philip2_escort", scene="global", label="philip_anal1_escort")

    $ questHelp("philip_10", True)
    $ autorun_to_object("ep217_dialogues5_phillip_3", scene="street_philiphome")
    $ add_hook("Teleport_Building", "ep217_dialogues5_phillip_4", scene="street_philiphome", label="private_presentation1_philip_block_after")
    call change_scene("street_philiphome", "Fade_long") from _rcall_change_scene_215
    return


label ep217_quests_philip2_escort: # приходит в эскорт
    $ remove_hook()
    fadeblack 1.5
    sound snd_fabric1
    pause 1.5

    call ep217_dialogues6_office_7() from _rcall_ep217_dialogues6_office_7
    $ questHelp("escort_18", True)

    call refresh_scene_fade() from _rcall_refresh_scene_fade_126
    return False
