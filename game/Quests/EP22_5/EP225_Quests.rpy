default ep225_quests_load_init_flag = False
label ep225_quests_load_init:
    if ep225_quests_load_init_flag == True:
        return
    $ ep225_quests_load_init_flag = True

    if ep224_quests_meeting2_day > 0 and ep224_quests_monica_kicked_client == 0:
        # Если была встреча с клиентом Эбби и Моника его не выгнала
        call ep225_quests_escort1_1_init()
    if ep224_quests_victoria_completed_day > 0:
        call ep225_quests_victoria_init()
    return



#
