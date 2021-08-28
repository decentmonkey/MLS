default ep219_quests_ralph_init_flag = False
default ep219_quests_ralph1_day = 0
default ep219_quests_ralph2_day = 0
default ep219_quests_ralph2_skip_day = 0
default ep219_quests_ralph3_last_day = 0

label ep219_quests_ralph_init1:
    if ep219_quests_ralph_init_flag == False:
        $ ep219_quests_ralph_init_flag = True
        $ questHelp("house_47")
        $ add_hook("change_time_day", "ep219_quests_ralph2_betty", scene="global", label="ep219_quests_ralph2_betty")
    return

label ep219_quests_ralph2_betty:
    if ep219_quests_ralph1_day == 0:
        $ ep219_quests_ralph1_day = day
        call ep219_dialogues1_ralph_1() from _rcall_ep219_dialogues1_ralph_1
        $ ep219_quests_ralph1_day = day
        $ questHelp("house_47", True)
        $ questHelp("house_47a")
        return
    if ep219_quests_ralph2_skip_day > day:
        return
    call ep219_dialogues1_ralph_2() from _rcall_ep219_dialogues1_ralph_2
    if _return == False:
        $ ep219_quests_ralph2_skip_day = day + 3
        return
    $ remove_hook()
    $ ep219_quests_ralph2_day = day
    $ questHelp("house_47a", True)
    if ep214_ralph_blowjob_day > 0: # Если Моника встречается с Ральфом
        $ questHelp("house_48")
    return

label ep219_quests_ralph3:
    call ep219_dialogues1_ralph_3() from _rcall_ep219_dialogues1_ralph_3 # анал с Ральфом
    if _return == False:
#        $ questHelp("house_48", False)
        return False
    $ questHelp("house_48", True)
    $ ep219_quests_ralph3_last_day = day
    $ monicaBettyRalphSeduction10 = True
    $ ep214_ralph_regular_noend_dialogue_day = day # пропускаем финальный диалог в этот день
    $ add_hook("enter_scene", "ep219_quests_ralph4_comment_after", scene="floor2", once=True, label="ep219_quests_ralph4_comment_after", priority = 200)

#    $ add_hook("enter_scene", "ep219_quests_ralph4_comment_after", scene="street_house_main_yard", label="ep219_quests_ralph4_comment_after")
    return

label ep219_quests_ralph4_comment_after:
    if monicaBettyRalphSeduction8 == True:
        call ep219_dialogues1_ralph_4() from _rcall_ep219_dialogues1_ralph_4
    else:
        call ep219_dialogues1_ralph_5() from _rcall_ep219_dialogues1_ralph_5
    return
