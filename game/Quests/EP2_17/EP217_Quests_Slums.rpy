default citizen5BlockedByDay = 0
default citizen5BForced = False
default citizen5LastDay = 0

default citizen9BlockedByDay = 0
default citizen9BForced = False
default citizen9LastDay = 0

label ep217_quests_slums1: # клик на Акира Сан
    call ep217_dialogues4_citizens_2() from _rcall_ep217_dialogues4_citizens_2
    if _return == -1: # не стала отходить с ним
        $ questHelp("work_slums_53", False, skipIfTrue=True)
        return
    if _return == -2: # пришли к пилону, но отказалась
        fadeblack 2.5
        $ questHelp("work_slums_53", False, skipIfTrue=True)
        call change_scene("hostel_edge_1_a", "Fade_long") from _rcall_change_scene_221
        return False

    $ set_active("Citizen_5", False, scene="all")
    $ citizen5BForced = False
    # идем в апартаменты
    $ questHelp("work_slums_53", True)
    $ citizen5BlockedByDay = day+3
    $ citizen5LastDay = day
    if _return == -3:
        call ep211_quests_slums_apartments2_check_enter_forced() from _rcall_ep211_quests_slums_apartments2_check_enter_forced_2
        $ monicaHomeLivingRoomMonicaSuffix = 5
        # прогнала
        $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="monicahome_livingroom")
        call change_scene("monicahome_livingroom", "Fade_long") from _rcall_change_scene_222
    call refresh_scene_fade() from _rcall_refresh_scene_fade_138
    return False


label ep217_quests_slums2: # клик на Найджела
    call ep217_dialogues4_citizens_1() from _rcall_ep217_dialogues4_citizens_1
    if _return == -1: # не стала отходить с ним
        $ questHelp("work_slums_52", False, skipIfTrue=True)
        return
    if _return == -2: # пришли к пилону, но отказалась
        fadeblack 2.5
        $ autorun_to_object("ep217_dialogues4_citizens_1b", scene="hostel_edge_1_a")
        $ questHelp("work_slums_52", False, skipIfTrue=True)
        call change_scene("hostel_edge_1_a", "Fade_long") from _rcall_change_scene_223
        return False

    $ set_active("Citizen_9", False, scene="all")
    $ citizen9BForced = False
    # идем в апартаменты
    $ questHelp("work_slums_52", True)
    $ citizen9BlockedByDay = day+3
    $ citizen9LastDay = day

    call ep217_dialogues4_citizens_1a() from _rcall_ep217_dialogues4_citizens_1a
    if _return == -1: # Моника отказалась участвовать в курении
        $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="street_monicahome")
        call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_224
        return False
    if _return == 1: # Моника имела секс с Филом
        pass
    if _return == 2: # Моника дала Филу косяк
        pass

    $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="street_monicahome")
    call change_scene("street_monicahome", "Fade_long") from _rcall_change_scene_225
#    call ep211_quests_slums_apartments2_check_enter_forced()
#    $ monicaHomeLivingRoomMonicaSuffix = 4
#    $ autorun_to_object("ep215_dialogues6_citizens_1c", scene="monicahome_livingroom")
#    call change_scene("monicahome_livingroom", "Fade_long")
    return False
