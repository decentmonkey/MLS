default ep218_quests_julia_init_flag = False
default ep218_quests_julia_active = False
default ep218_quests_julia_last_day = 0
default ep218_quests_julia_completed_last_day = 0

label ep218_quests_julia_init:
    if ep218_quests_julia_init_flag == True:
        return
    if monica_living_at_juliahome == True and juliaQuestMonicaRefusedFred == False and juliaQuestRefused == False:
        $ ep218_quests_julia_init_flag = True
        $ questHelp("julia_56")
        $ ep218_quests_julia_active = True
    return

label ep218_quests_julia1: # разговор с Юлией в воскресенье днем
    $ ep218_quests_julia_last_day = day
    call ep218_dialogues5_julia_1() from _rcall_ep218_dialogues5_julia_1
    if _return == False:
        $ cloth = monica_juliahome_outside_cloth
        $ cloth_type = monica_juliahome_outside_cloth_type
        $ juliaQuestRefused = True
        call ep218_quests_abort_julia() from _rcall_ep218_quests_abort_julia
        call bitch(20, "abort_julia") from _rcall_bitch_22
        $ autorun_to_object("ep218_dialogues5_julia_4b", scene="street_house_outside")
        call process_change_map_location("House") from _rcall_process_change_map_location_11
        call change_scene("street_house_outside", "Fade_long") from _rcall_change_scene_230
        return False
    call ep218_dialogues5_julia_3() from _rcall_ep218_dialogues5_julia_3
    if _return == False:
        $ questHelp("julia_56", False, skipIfTrue = True)
        $ cloth = monica_juliahome_outside_cloth
        $ cloth_type = monica_juliahome_outside_cloth_type
        $ autorun_to_object("ep218_dialogues5_julia_4b", scene="street_juliahome")
        music2 stop
        call change_scene("street_juliahome", "Fade_long") from _rcall_change_scene_231
        return False
    $ cloth = monica_juliahome_outside_cloth
    $ cloth_type = monica_juliahome_outside_cloth_type
    $ autorun_to_object("ep218_dialogues5_julia_4", scene="street_juliahome")
    $ ep218_quests_julia_completed_last_day = day
    call ep224_quests_julia_init() from _rcall_ep224_quests_julia_init_1
    $ add_char_progress("Julia", 30, "julia_dating_park1")
    $ char_info["Julia"]["caption"] = t_("Юлия любит Монику и подумывает о свадьбе с ней.")
    $ questHelp("julia_56", True)
    music2 stop
    call change_scene("street_juliahome", "Fade_long") from _rcall_change_scene_232
    return False

label ep218_quests_abort_julia:
    python:
        char_info["Julia"]["level"] = 1
        char_info["Julia"]["current_progress"] = 0
        char_info["Julia"]["caption"] = t_("Юлия боится Монику")
        minimapJuliaGenerateEnabled = False
        clear_hooks("Julia", scene="working_office_cabinet")
        add_hook("Julia", "ep26_quests_office7", scene="working_office_cabinet")
        monica_living_at_juliahome = False
        questLog(64, False)
        questLog(73, False)
        questLog(74, False)
        remove_hook(quest="juliahome")
        questsFailByCategory(t_("ЮЛИЯ"))
    return
















#
