default ep225_quests_victoria_init_flag = False
default ep225_quests_victoria_completed_day = 0
default ep225_quests_victoria_stage = 0
label ep225_quests_victoria_init:
    if ep225_quests_victoria_init_flag == True:
        return
    $ ep225_quests_victoria_init_flag = True
    $ questHelp("victoria_20")
    $ add_hook("office_work_process", "ep225_quests_victoria_2", scene="global", label="ep225_quests_victoria_2", priority=1)
    return

label ep225_quests_victoria_2: # Диалог у Виктории дома
    if ep225_quests_victoria_stage == 0:
        call ep22_5_dialogues3_melanie_1()
        $ move_object("Melanie", "empty")
        $ Melanie_Life_evening2_skip_once = True
        $ ep225_quests_victoria_stage = 1
        $ questHelp("victoria_20", True)
        $ questHelp("victoria_21")
        return
    if ep225_quests_victoria_stage == 1:
#        $ remove_hook()
        call ep22_5_dialogues3_melanie_2()
        $ ep225_quests_victoria_completed_day = day
        $ ep225_quests_victoria_stage = 2
        $ Melanie_Life_evening2_skip_once = True
        $ move_object("Melanie", "empty")
        $ move_object("AlexPhotograph", "empty")
        $ questHelp("victoria_21", True)
        $ add_hook("change_time_day", "ep225_quests_victoria_3", scene="global", once=True)
        fadeblack 2.0
        return
    return

label ep225_quests_victoria_3:
    # Возвращаем Алекса
    $ move_object("AlexPhotograph", "monica_office_photostudio")
    return
