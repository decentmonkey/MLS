default ep224_quests_victoria_init_flag = False
default ep224_quests_victoria_completed_day = 0
label ep224_quests_victoria_init:
    if ep224_quests_victoria_init_flag == True:
        return
    $ questHelp("victoria_19")
    $ ep224_quests_victoria_init_flag = True
    $ add_hook("office_work_process", "ep224_quests_victoria1_fitness", scene="global", label="ep224_quests_victoria1_fitness", priority=1)
    return

label ep224_quests_victoria1_fitness:
    if week_day == 2 or week_day == 4:
        return
    $ remove_hook()
    call ep22_4_dialogues2_fitness_1() from _rcall_ep22_4_dialogues2_fitness_1
    call ep22_4_dialogues2_fitness_2() from _rcall_ep22_4_dialogues2_fitness_2
    call ep22_4_dialogues2_fitness_3() from _rcall_ep22_4_dialogues2_fitness_3
    $ ep224_quests_victoria_completed_day = day
    $ questHelp("victoria_19", True)
    call ep225_quests_victoria_init()
    return
