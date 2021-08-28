label process_afterload:
    if monicaWorkingAtBiffOffice == False and monicaOutfitsEnabled[6] == True:
        $ remove_hook(label="biff_work_dialogue1")
        $ ep26_quests_biff1_Flag = False
        call ep26_quests_biff1() from _call_ep26_quests_biff1_1

    call ep28_quests() from _call_ep28_quests
    call ep29_quests_init() from _rcall_ep29_quests_init
    call ep29_revenge_quest1_init() from _rcall_ep29_revenge_quest1_init
    call monica_cheats_init() from _rcall_monica_cheats_init
    call ep210_quests_load_init() from _rcall_ep210_quests_load_init
    call ep211_quests_load_init() from _rcall_ep211_quests_load_init
    call ep212_quests_load_init() from _rcall_ep212_quests_load_init
    call ep213_quests_load_init() from _rcall_ep213_quests_load_init
    call ep214_quests_load_init() from _rcall_ep214_quests_load_init
    call ep215_quests_load_init() from _rcall_ep215_quests_load_init
    call ep216_quests_load_init() from _rcall_ep216_quests_load_init
    return

label process_afterload_part2:
    if scenes_data.has_key("misc") == False or scenes_data["misc"].has_key("list_type") == False:
        $ scenes_data["misc"] = {"list_type": ["item1", "item2"]}
    call questLog_init() from _rcall_questLog_init
    call questHelp_init() from _rcall_questHelp_init
    call ep217_quests_bugfix1() from _rcall_ep217_quests_bugfix1
    call ep218_quests_load_init() from _rcall_ep218_quests_load_init
    call ep219_quests_load_init() from _rcall_ep219_quests_load_init
    call ep224_quests_load_init() from _rcall_ep224_quests_load_init
    call ep225_quests_load_init()
    return
