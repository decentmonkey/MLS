default ep218_quests_betty_inited = False
default ep218_quests_betty_inited2 = False

default ep218_quests_betty_day = 0
default ep218_quests_betty_completed_day = 0

label ep218_quests_betty_init:
    if ep218_quests_betty_inited == True:
        return
    $ add_hook("fitness_end", "ep218_quests_betty1_check", scene="global", label="betty_neighbour_check")
    $ ep218_quests_betty_inited = True
    $ questHelp("house_46", skipIfExists = True)
    return

label ep218_quests_betty1_check:
    if ep218_quests_betty_inited2 == True:
        return
    $ ep218_quests_betty_inited2 = True
    $ remove_hook(label="betty_neighbour_check")
    $ add_hook("change_time_day", "ep218_quests_betty2_begin", scene="global", label="ep218_quests_betty2_begin", priority = 1)

    return

label ep218_quests_betty2_begin:
    $ remove_hook()
    $ ep218_quests_betty_day = day
    call ep218_dialogues4_betty_1() from _rcall_ep218_dialogues4_betty_1
    if _return == False:
        $ questHelp("house_46", False)
        return

    call ep218_dialogues4_betty_1a1() from _rcall_ep218_dialogues4_betty_1a1
    call ep218_dialogues4_betty_1a() from _rcall_ep218_dialogues4_betty_1a
    call ep218_dialogues4_betty_2() from _rcall_ep218_dialogues4_betty_2
    if _return == False:
        $ questHelp("house_46", False)
        return
    call ep218_dialogues4_betty_3() from _rcall_ep218_dialogues4_betty_3
    call ep218_dialogues4_betty_4() from _rcall_ep218_dialogues4_betty_4 # дом соседа
    call ep218_dialogues4_betty_5() from _rcall_ep218_dialogues4_betty_5
    if _return == False:
        $ questHelp("house_46", False)
        return
    call ep218_dialogues4_betty_6() from _rcall_ep218_dialogues4_betty_6 # заходит Ральф
    $ ep218_quests_betty_completed_day = day
    $ questHelp("house_46", True)
    call ep219_quests_ralph_init1() from _rcall_ep219_quests_ralph_init1_1
    call ep224_quests_betty_init() from _rcall_ep224_quests_betty_init_1
    return
















#
